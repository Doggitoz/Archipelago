from BaseClasses import Item, ItemClassification
from typing import Dict, List, TYPE_CHECKING
from .Types import ItemData, ArchipelaCodeItem
from .Locations import get_total_locations

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld
    
def create_itempool(world: "ArchipelaCodeWorld") -> List[Item]:
    itempool: List[Item] = []
    
    for name in item_table.keys():
        data = item_table.get(name)
        
        if data is None:
            continue
        
        item_type: ItemClassification = item_table.get(name).classification
        
        if item_type is ItemClassification.filler or item_type is ItemClassification.trap:
            continue
        
        if data.language == "py" and not world.options.EnablePython:
            continue
        
        if data.language == "js" and not world.options.EnableJavascript:
            continue
        
        
        itempool += create_multiple_items(world, name, item_frequencies.get(name, 1), item_type)
        
    
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool))
    return itempool

def create_item(world: "ArchipelaCodeWorld", name: str) -> Item:
    data = item_table[name]
    return ArchipelaCodeItem(name, data.classification, data.code, world.player)

def create_multiple_items(world: "ArchipelaCodeWorld", name: str, count: int = 1, item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    return [ArchipelaCodeItem(name, item_type, data.code, world.player) for _ in range(count)] 
        

def create_junk_items(world: "ArchipelaCodeWorld", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    ic: ItemClassification
    
    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)
            
    for _ in range(count):
        junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))
        
    return junk_pool

junk_items = { # 1000 range for junk items
    "Github Copilot": ItemData(6700901000, ItemClassification.filler, "junk"),
    "Claude Code": ItemData(6700901001, ItemClassification.filler, "junk"),
    "Cursor": ItemData(6700901002, ItemClassification.filler, "junk"),
    "Google Jules": ItemData(6700901003, ItemClassification.filler, "junk"),
    "Gemini Code Assist": ItemData(6700901004, ItemClassification.filler, "junk"),
    "ChatGPT": ItemData(6700901005, ItemClassification.filler, "junk"),
    "Aider": ItemData(6700901006, ItemClassification.filler, "junk")
}

misc_items = { # 2000 range for misc items
    "Progressive Line Count": ItemData(6700902000, ItemClassification.progression, "misc"),
    "Progressive Character Limit": ItemData(6700902001, ItemClassification.progression, "misc"),
    "Progressive Difficulty Unlock": ItemData(6700902002, ItemClassification.progression, "misc")
}

python_items = { # 3100 range for Python items
    "Python 'if'": ItemData(6700903100, ItemClassification.progression, "py"),
    "Python 'for'": ItemData(6700903101, ItemClassification.useful, "py"),
    "Python '='": ItemData(6700903102, ItemClassification.progression, "py")
}

apcode_items = { # 6700900000 range for items
    **junk_items, # 1000
    **misc_items, # 2000
    **python_items # 3100
}

item_table = {
    **apcode_items
}

item_frequencies = {
    "Progressive Difficulty Unlock": 2
}

junk_weights = {
    "Github Copilot": 50,
    "Claude Code": 50,
    "Cursor": 50,
    "Google Jules": 50,
    "Gemini Code Assist": 50,
    "ChatGPT": 50,
    "Aider": 50
}