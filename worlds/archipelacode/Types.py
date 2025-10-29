from dataclasses import dataclass
from typing import Dict, List, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, Location


class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    language: str = ""


class LocData(NamedTuple):
    id: int = 0
    name: str = "New Location"
    title_slug: str = "new-location"
    difficulty: str = "EASY"
    lang_slugs: List[str] = []  # List of langSlugs
    required_features: Dict[
        str, List[int]
    ] = {}  # {langSlug: [<Required lang feature 1 item id>, <Required lang feature 2 item id>]}


class ArchipelaCodeItem(Item):
    game = "ArchipelaCode"


class ArchipelaCodeLocation(Location):
    game = "ArchipelaCode"


@dataclass
class Language:
    lang: str
    langSlugs: List[str]


@dataclass
class VersionIdentifier:
    major: int
    minor: int
    patch: int
