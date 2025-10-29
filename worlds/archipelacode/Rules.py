from typing import TYPE_CHECKING, List, Dict
from worlds.AutoWorld import CollectionState
from worlds.generic.Rules import add_rule
from .Items import get_item_name_from_id

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld

def check_if_location_is_available(world: "ArchipelaCodeWorld", state: CollectionState, required_features: Dict[str, List[int]]) -> bool:        
    return any([all([state.has(get_item_name_from_id(item_id), world.player) for item_id in lang_features]) for lang_features in required_features.values()])

def has_reached_goal(world: "ArchipelaCodeWorld", state: CollectionState) -> bool:
    required_problems: int = world.options.EndGoal.value
    return len(state.locations_checked) >= required_problems

def set_rules(world: "ArchipelaCodeWorld") -> None:
    add_rule(
        world.multiworld.get_entrance(
            "Starter Problems -> Extra Problem Batch 1", world.player
        ),
        lambda state: state.has("Progressive Problem Unlock", world.player, 1),
    )
    add_rule(
        world.multiworld.get_entrance(
            "Extra Problem Batch 1 -> Extra Problem Batch 2", world.player
        ),
        lambda state: state.has("Progressive Problem Unlock", world.player, 2),
    )
    add_rule(
        world.multiworld.get_entrance(
            "Extra Problem Batch 2 -> Extra Problem Batch 3", world.player
        ),
        lambda state: state.has("Progressive Problem Unlock", world.player, 3),
    )
    add_rule(
        world.multiworld.get_entrance(
            "Extra Problem Batch 3 -> Extra Problem Batch 4", world.player
        ),
        lambda state: state.has("Progressive Problem Unlock", world.player, 4),
    )
    
    for location in world.included_locations:
        add_rule(
            world.multiworld.get_location(location.name, world.player),
            lambda state: check_if_location_is_available(world, state, location.required_features)
        )

    world.multiworld.completion_condition[world.player] = (
        lambda state: has_reached_goal(world, state)
    )
