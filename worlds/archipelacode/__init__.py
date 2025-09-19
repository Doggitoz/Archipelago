from BaseClasses import MultiWorld, Item
from worlds.AutoWorld import World, WebWorld
from .Options import APCodeOptions
from .Items import item_table, create_itempool, junk_weights, create_item
from .Locations import get_location_names
from .Regions import create_regions

class ArchiwebaCode(WebWorld):
    theme = "partyTime"

class ArchipelaCodeWorld(World):
    """ArchipelaCode is an AP implementation for VS Code and LeetCode."""
    game = "ArchipelaCode"
    web = ArchiwebaCode()
    options_dataclass = APCodeOptions
    options = APCodeOptions
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = get_location_names() 
    
    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        
    def create_item(self, name: str) -> Item:
        return create_item(self, name)
        
    def create_items(self):
        self.multiworld.itempool += create_itempool(self)
        
    def get_filler_item_name(self) -> str:
        return self.random.choices(list(junk_weights.keys()), weights=junk_weights.values(), k=1)[0]
    
    def create_regions(self):
        create_regions(self)