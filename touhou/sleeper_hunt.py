from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SleeperHuntArchipelagoOptions:
    pass

class SleeperHuntGame(Game):
    name = "Sleeper Hunt (Touhou Artificial Dream in Arcadia)"
    platform = KeymastersKeepGamePlatforms.PC
    
    platforms_other= [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW
    ]

    is_adult_only_or_unrated = False

    options_cls = SleeperHuntArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Enable the TYPE Grimore",
                data={
                    "TYPE": (self.yokai_grimores, 1),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return[
            GameObjectiveTemplate(
                label="Hijack a/an RACE sleeper",
                data={
                    "RACE": (self.sleeper_races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Hijack a sleeper with the that has a AFFINITY affinity to ELEMENT",
                data={
                    "AFFINITY": (self.elements_affinities, 1),
                    "ELEMENT":  (self.elements, 1)
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Hijack a sleeper with the that has a AFFINITY affinity to Physical",
                data={
                    "AFFINITY": (self.element_physical_affinities, 1),
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Hijack a sleeper with the that has a AFFINITY affinity to Electric",
                data={
                    "AFFINITY": (self.element_electric_affinities, 1),
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Fuse sleepers to make a/an RACE sleeper",
                data={
                    "RACE": (self.sleeper_races, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Fuse sleepers to make a sleeper with the that has a AFFINITY affinity to ELEMENT",
                data={
                    "AFFINITY": (self.elements_affinities, 1),
                    "ELEMENT":  (self.elements, 1)
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Fuse sleepers to make a sleeper with the that has a AFFINITY affinity to Physical",
                data={
                    "AFFINITY": (self.element_physical_affinities, 1),
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Fuse sleepers to make a sleeper with the that has a AFFINITY affinity to Electric",
                data={
                    "AFFINITY": (self.element_electric_affinities, 1),
                },  
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

    @staticmethod
    def yokai_grimores() -> List[str]:
        return [
            "Easy",
            "Lunatic",
            "Negotiation",
            "Loner",
            "Sting",
            "Dilema",
            "Power",
            "Aggression",
            "Compassion",
            "Explorer",
        ]
    
    @staticmethod
    def sleeper_races() -> List[str]:
        return[
            "Alien",
            "Celestial",
            "Deity",
            "Demon",
            "Human",
            "Nature",
            "Oni",
            "Undead",
            "Unknown",
            "Vampire",
            "Witch",
            "Yokai",
        ]
    
    @staticmethod
    def elements() -> List[str]:
        return[
            "Piercing",
            "Fire",
            "Ice",
            "Force",
            "Mind",
        ]
    
    @staticmethod
    def elements_affinities() -> List[str]:
        return [
            "Weak",
            "Neutral",
            "Resistant",
            "Null",
            "Drain",
        ]
    
    @staticmethod
    def element_physical_affinities() -> List[str]:
        return [
            "Weak",
            "Neutral",
            "Resistant",
            "Drain",
        ]
    
    @staticmethod
    def element_electric_affinities() -> List[str]:
        return [
            "Weak",
            "Neutral",
            "Resistant",
            "Drain",
        ]
    

