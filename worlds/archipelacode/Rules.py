from typing import TYPE_CHECKING
from worlds.AutoWorld import CollectionState
from worlds.generic.Rules import add_rule, set_rule

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
