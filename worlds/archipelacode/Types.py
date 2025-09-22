from typing import NamedTuple, Optional, Dict, List
from BaseClasses import Location, Item, ItemClassification
from dataclasses import dataclass


class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    language: str = ""


class LocData(NamedTuple):
    id: int = 0
    name: str = "New Item"
    title_slug: str = "new-item"
    difficulty: str = "EASY"
    lang_slugs: List[str] = [] # List of langSlugs
    required_features: Dict[str, List[int]] = {} # {langSlug: [<Required lang feature 1 item id>, <Required lang feature 2 item id>]}


class ArchipelaCodeItem(Item):
    game = "ArchipelaCode"


class ArchipelaCodeLocation(Location):
    game = "ArchipelaCode"

@dataclass
class Language:
    lang: str
    langSlugs: List[str]
