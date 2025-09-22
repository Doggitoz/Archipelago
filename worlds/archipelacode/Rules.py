from typing import TYPE_CHECKING
from worlds.AutoWorld import CollectionState
from worlds.generic.Rules import add_rule
from .Items import get_item_name_from_id

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld


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
        for langSlug, features in location.required_features.items():
            for item_id in features:
                add_rule(
                    world.multiworld.get_location(location.name, world.player),
                    lambda state: state.has(
                        get_item_name_from_id(item_id), world.player
                    ),
                )

    world.multiworld.completion_condition[world.player] = (
        lambda state: has_reached_goal(world, state)
    )


def has_reached_goal(world: "ArchipelaCodeWorld", state: CollectionState) -> bool:
    required_problems: int = world.options.EndGoal.value
    return len(state.locations_checked) >= required_problems
