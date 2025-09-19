from typing import NamedTuple, Optional

from BaseClasses import Location, Item, ItemClassification

class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    language: str = ""

class LocData(NamedTuple):
    id: int = 0
    name: str = "New Item"
    title_slug: str = "new-item"
    difficulty: str = "EASY"
    
class ArchipelaCodeItem(Item):
    game = "ArchipelaCode"
    
class ArchipelaCodeLocation(Location):
    game = "ArchipelaCode"