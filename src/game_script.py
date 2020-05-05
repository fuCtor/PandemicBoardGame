from dataclasses import dataclass
from typing import Any, Set, Mapping, List

@dataclass
class GameScript:
    cities: Mapping[str, Any]
    connections: Mapping[str, List[str]]
    colors: Set[str]
    diseases: Set[str]

    rate: List[int]
    initial_city: str = ""
    epidemics: int = 0    
    cubes: int = 0
    min_players: int = 0
    max_players: int = 0
    max_player_actions: int = 0
    
    outbreak_initial_level: int = 0
    outbreak_death_level: int = 0
