from typing import NamedTuple, Optional

from BaseClasses import Location, Item, ItemClassification

class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    language: str = ""

class LocData(NamedTuple):
    id: int = 0
    name: str = "New Item"
    region: str = "Menu"
    
class ArchipelaCodeItem(Item):
    game = "ArchipelaCode"
    
class ArchipelaCodeLocation(Location):
    game = "ArchipelaCode"