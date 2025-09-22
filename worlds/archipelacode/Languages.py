from .Types import Language
from typing import List

def get_all_supported_languages() -> List[Language]:
    return [
        Language("Python3", ["python3"]),
        Language("Javascript", ["javascript"]),
    ]