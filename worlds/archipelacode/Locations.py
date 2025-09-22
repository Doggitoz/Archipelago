from typing import Dict, TYPE_CHECKING
from .Types import LocData
import json
from pathlib import Path

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld


def generate_locations() -> list[(str, LocData)]:
    curr_path = Path(__file__).resolve()
    curr_dir = curr_path.parent
    data_file_path = curr_dir / "data" / "ap_locations.json"

    with open(data_file_path, "r") as f:
        data = json.load(f)
        f.close()

    output = []

    for id, problem in data.items():
        output.append((problem["titleSlug"], LocData(int(id), problem["title"], problem["titleSlug"], problem["difficulty"], problem["langSlugs"], problem["required_features"])))

    return output


def get_location_names() -> Dict[str, int]:
    location_table = get_location_table()
    names = {data.name: data.id for name, data in location_table.items()}
    return names


def get_total_locations(world: "ArchipelaCodeWorld") -> int:
    location_table = get_location_table()
    total = 0

    total += len(location_table)

    return total


def get_location_table() -> Dict[str, LocData]:
    apcode_locations = {f"{id}": problem for id, problem in generate_locations()}
    location_table = {**apcode_locations}
    return location_table