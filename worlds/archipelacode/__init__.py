from BaseClasses import MultiWorld, Item
from worlds.AutoWorld import World, WebWorld
from typing import Dict, List
from .Options import APCodeOptions
from .Items import item_table, create_itempool, junk_weights, create_item
from .Locations import get_location_names, get_location_table
from .Regions import create_regions
from .Types import LocData, Language
from .Rules import set_rules
from .Helpers import split_array


class ArchiwebaCode(WebWorld):
    theme = "partyTime"


class ArchipelaCodeWorld(World):
    """ArchipelaCode is an AP implementation for VS Code and LeetCode."""

    game = "ArchipelaCode"
    web = ArchiwebaCode()
    options_dataclass = APCodeOptions
    options: APCodeOptions = APCodeOptions
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = get_location_names()

    included_locations: List[LocData] = []
    included_languages: List[Language] = []

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def get_filler_item_name(self) -> str:
        return self.random.choices(
            list(junk_weights.keys()), weights=junk_weights.values(), k=1
        )[0]

    def create_regions(self):
        create_regions(self)

    def generate_early(self):
        if self.options.EnablePython:
            self.included_languages.append(Language("Python3", ["python3"]))
        if self.options.EnableJavascript:
            self.included_languages.append(Language("Javascript", ["javascript"]))
        
        easy_locations: List[LocData] = []
        medium_locations: List[LocData] = []
        hard_locations: List[LocData] = []
        for _, data in get_location_table().items():
            included_slugs: List[str] = []
            for langSlug in data.lang_slugs:
                for lang in self.included_languages:
                    if langSlug in lang.langSlugs:
                        included_slugs.append(langSlug)
            if len(included_slugs) == 0:
                continue
            new_loc = LocData(data.id, data.name, data.title_slug, data.difficulty, included_slugs, data.required_features)
            match data.difficulty:
                case "EASY":
                    easy_locations.append(new_loc)
                case "MEDIUM":
                    medium_locations.append(new_loc)
                case "HARD":
                    hard_locations.append(new_loc)
        
        self.included_locations.extend(self.random.choices(easy_locations, k=round(self.options.TotalProblemCount * 0.4)))
        self.included_locations.extend(self.random.choices(medium_locations, k=round(self.options.TotalProblemCount * 0.3)))
        self.included_locations.extend(self.random.choices(hard_locations, k=round(self.options.TotalProblemCount * 0.3)))
        
        self.included_locations = self.lightly_shuffle(self.included_locations, 0.08) # Makes it so you don't only get easy problems in the first few batches, while still giving you generally easier problems at the start
        
        for _ in range(3): # it's 4 AM and I'm too tired to figure out a better solution. I don't even know why it's happening. - ShackledMars261, 9/19/25 4:19 AM
            dupe_check: list[str] = []
            easys_to_add: int = 0
            mediums_to_add: int = 0
            hards_to_add: int = 0
            for index, loc in enumerate(self.included_locations):
                if loc.name not in dupe_check:
                    dupe_check.append(loc.name)
                    continue
                self.included_locations.pop(index)
                match loc.difficulty:
                    case "EASY":
                        easys_to_add += 1
                    case "MEDIUM":
                        mediums_to_add += 1
                    case "HARD":
                        hards_to_add += 1
            
            for _ in range(easys_to_add):
                self.included_locations.append(self.random.choice(easy_locations))
            for _ in range(mediums_to_add):
                self.included_locations.append(self.random.choice(medium_locations))
            for _ in range(hards_to_add):
                self.included_locations.append(self.random.choice(hard_locations))
        

    def set_rules(self):
        set_rules(self)
        
    def fill_slot_data(self):
        loc_arrays = split_array(self.included_locations, 5)
        slot_data: Dict[str, any] = {"regions": {}, "metadata": {"included_languages": {}}}
        for index, array in enumerate(loc_arrays):
            slot_data["regions"][str(index)] = {}
            for loc in array:
                slot_data["regions"][str(index)][loc.id] = {"id": int(loc.id), "title": loc.name, "titleSlug": loc.title_slug, "difficulty": loc.difficulty}
                
        slot_data["metadata"]["EndGoal"] = int(self.options.EndGoal.value)
        
        slot_data["metadata"]["included_languages"]["python3"] = True if self.options.EnablePython else False
        slot_data["metadata"]["included_languages"]["javascript"] = True if self.options.EnableJavascript else False
        
        print(f"Python {"Enabled" if self.options.EnablePython else "Disabled"}")
        print(f"Javascript {"Enabled" if self.options.EnableJavascript else "Disabled"}")
                
        return slot_data
    
    def lightly_shuffle(self, orig_list: List, orderliness: float = 0.2) -> List:
        return sorted(orig_list, key=lambda i: self.random.gauss(orig_list.index(i) * orderliness, 1))