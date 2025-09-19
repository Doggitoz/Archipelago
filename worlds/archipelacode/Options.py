from worlds.AutoWorld import PerGameCommonOptions
from typing import List, TYPE_CHECKING, Dict, Any
from dataclasses import dataclass
from Options import Range, OptionGroup, StartInventoryPool, Toggle, DefaultOnToggle

if TYPE_CHECKING:
    from . import ArchipelaCodeWorld

def create_options_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in apcode_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))
    
    return option_group_list

def adjust_options(world: "ArchipelaCodeWorld"):
    pass

class EndGoal(Range):
    """How many problems are needed to be solved to \"win\" the game."""
    display_name = "End Goal"
    range_start = 1
    range_end = 100
    default = 15
    
class TotalProblemCount(Range):
    """How many total problems to include."""
    display_name = "Total Problems"
    range_start = 10
    range_end = 200
    default = 50
    
class EnablePython(DefaultOnToggle):
    """Whether or not to include the Python language."""
    display_name = "Enable Python"
    
class EnableJavascript(Toggle):
    """Whether or not to include the Javascript language."""
    display_name = "Enable Javascript"

@dataclass
class APCodeOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    
    EndGoal: EndGoal
    
    TotalProblemCount: TotalProblemCount
    
    EnablePython: EnablePython
    EnableJavascript: EnableJavascript

apcode_option_groups: Dict[str, List[Any]] = {}