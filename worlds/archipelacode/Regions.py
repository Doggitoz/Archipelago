from typing import TYPE_CHECKING
from BaseClasses import Region
from .Locations import get_location_table
from .Types import ArchipelaCodeLocation

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld

def create_regions(world: "ArchipelaCodeWorld"):
    menu = create_region(world, "Menu")

def create_region(world: "ArchipelaCodeWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)
    
    for (key, data) in get_location_table().items():
        if data.region == name:
            loc = ArchipelaCodeLocation(world.player, data.name, data.id, reg)
            reg.locations.append(loc)
            
    world.multiworld.regions.append(reg)
    return reg