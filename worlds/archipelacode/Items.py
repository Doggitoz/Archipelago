from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .Types import ArchipelaCodeItem, ItemData

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld


def create_itempool(world: "ArchipelaCodeWorld") -> list[Item]:
    itempool: list[Item] = []

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

        if data.language == "ts" and not world.options.EnableTypescript:
            continue

        if data.language == "go" and not world.options.EnableGolang:
            continue

        itempool += create_multiple_items(world, name, item_frequencies.get(name, 1), item_type)

    itempool += create_junk_items(world, len(world.included_locations) - len(itempool))
    return itempool


def create_item(world: "ArchipelaCodeWorld", name: str) -> Item:
    data = item_table[name]
    return ArchipelaCodeItem(name, data.classification, data.code, world.player)


def create_multiple_items(
    world: "ArchipelaCodeWorld",
    name: str,
    count: int = 1,
    item_type: ItemClassification = ItemClassification.progression,
) -> list[Item]:
    data = item_table[name]
    return [ArchipelaCodeItem(name, item_type, data.code, world.player) for _ in range(count)]


def create_junk_items(world: "ArchipelaCodeWorld", count: int) -> list[Item]:
    junk_pool: list[Item] = []
    junk_list: dict[str, int] = {}
    ic: ItemClassification

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

    for _ in range(count):
        junk_pool.append(
            world.create_item(world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0])
        )

    return junk_pool


def get_item_name_from_id(id: int) -> str:
    for item_name, item in item_table.items():
        if item.code == id:
            return item_name


junk_items = {  # 1000 range for junk items
    "Github Copilot": ItemData(6700901000, ItemClassification.filler, "junk"),
    "Claude Code": ItemData(6700901001, ItemClassification.filler, "junk"),
    "Cursor": ItemData(6700901002, ItemClassification.filler, "junk"),
    "Google Jules": ItemData(6700901003, ItemClassification.filler, "junk"),
    "Gemini Code Assist": ItemData(6700901004, ItemClassification.filler, "junk"),
    "ChatGPT": ItemData(6700901005, ItemClassification.filler, "junk"),
    "Aider": ItemData(6700901006, ItemClassification.filler, "junk"),
}

misc_items = {  # 2000 range for misc items
    "Progressive Line Count": ItemData(6700902000, ItemClassification.progression, "misc"),
    "Progressive Character Limit": ItemData(6700902001, ItemClassification.progression, "misc"),
    "Progressive Problem Unlock": ItemData(6700902002, ItemClassification.progression, "misc"),
}

python_items = {  # 3100 range for Python items
    "Python 'if'": ItemData(6700903100, ItemClassification.progression, "py"),
    "Python 'for'": ItemData(6700903101, ItemClassification.useful, "py"),
    "Python '='": ItemData(6700903102, ItemClassification.progression, "py"),
    "Python Comparison Operators": ItemData(6700903103, ItemClassification.progression, "py"),
    "Python 'while'": ItemData(6700903104, ItemClassification.useful, "py"),
    "Python 'else'": ItemData(6700903105, ItemClassification.useful, "py"),
    "Python 'elif'": ItemData(6700903106, ItemClassification.useful, "py"),
    "Python 'match'": ItemData(6700903107, ItemClassification.useful, "py"),
    "Python '+'": ItemData(6700903108, ItemClassification.progression, "py"),
    "Python '-'": ItemData(6700903109, ItemClassification.progression, "py"),
    "Python '*'": ItemData(6700903110, ItemClassification.progression, "py"),
    "Python '/'": ItemData(6700903111, ItemClassification.progression, "py"),
    "Python '**'": ItemData(6700903112, ItemClassification.useful, "py"),
    "Python '//'": ItemData(6700903113, ItemClassification.useful, "py"),
    "Python '%'": ItemData(6700903114, ItemClassification.useful, "py"),
    "Python 'and'": ItemData(6700903115, ItemClassification.useful, "py"),
    "Python 'or'": ItemData(6700903116, ItemClassification.progression, "py"),
    "Python 'not'": ItemData(6700903117, ItemClassification.progression, "py"),
    "Python 'is'": ItemData(6700903118, ItemClassification.useful, "py"),
    "Python 'in'": ItemData(6700903119, ItemClassification.useful, "py"),
}

apcode_items = {  # 6700900000 range for items
    **junk_items,  # 1000
    **misc_items,  # 2000
    **python_items,  # 3100
}

item_table = {**apcode_items}

item_frequencies = {"Progressive Problem Unlock": 4}

junk_weights = {
    "Github Copilot": 50,
    "Claude Code": 50,
    "Cursor": 50,
    "Google Jules": 50,
    "Gemini Code Assist": 50,
    "ChatGPT": 50,
    "Aider": 50,
}
