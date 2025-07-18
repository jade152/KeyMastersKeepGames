from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class ForsakenGameArchipelagoOptions:
    forsaken_survivors_owned: ForsakenSurviorsOwned
    forsaken_killers_owned: ForsakenKillersOwned


class ForsakenGame(Game):
    name = "Forsaken (Roblox)"

    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
    ]

    is_adult_only_or_unrated = False

    options_cls = ForsakenGameArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Play with the following restriction in this keep: RESTRICTION",
                data={
                    "RESTRICTION": (self.restrictions, 1),
                },
            ),
            ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Survive a round as SURVIVOR",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a round as KILLER",
                data={
                    "KILLER": (self.killers, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Survive COUNT rounds as SURVIVOR",
                data={
                    "SURVIVOR": (self.survivors, 1),
                    "COUNT": (self.round_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win COUNT rounds as KILLER",
                data={
                    "KILLER": (self.killers, 1),
                    "COUNT": (self.round_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete COUNT generator puzzles",
                data={
                    "COUNT": (self.puzzle_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Survive a round with KILLER present",
                data={
                    "KILLER": (self.killers, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a round in MAP",
                data={
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win COUNT rounds in MAP",
                data={
                    "MAP": (self.maps, 1),
                    "COUNT": (self.round_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            ]

    @staticmethod
    def maps() -> List[str]:
        return [
            "Brandon6875935\'s Place",
            "Yorick\'s Resting Place",
            "Glass Houses",
            "Horror Hotel",
            "Planet Voss",
            "Ultimate Assassin Grounds",
            "Pirate Bay",
            "Underground War",
            "C00l Carnival",
            ]

    @staticmethod
    def restrictions() -> List[str]:
        return [
            "Walk only",
            "Don't use active abilities",
            ]

    @staticmethod
    def round_range() -> range:
        return range(1, 10)

    @staticmethod
    def puzzle_range() -> range:
        return range(1, 6)

    def survivors(self) -> List[str]:
        return sorted(self.archipelago_options.forsaken_survivors_owned)

    def killers(self) -> List[str]:
        return sorted(self.archipelago_options.forsaken_killers_owned)

# Archipelago Options
class ForsakenSurviorsOwned(OptionSet):
    """
    Indicates which survivor characters the player owns and wants to possibly play as.
    """
    display_name = "Forsaken Survivors Owned"
    valid_keys = [
        "Noob",
        "007n7",
        "Shedletsky",
        "Guest 1337",
        "Chance",
        "Two Time",
        "Elliot",
        "Dusekkar",
        "Builderman",
        "Taph",
    ]

    default = valid_keys


class ForsakenKillersOwned(OptionSet):
    """
    Indicates which killer characters the player owns and wants to possibly play as.
    """
    display_name = "Forsaken Killers Owned"
    valid_keys = [
        "Jason",
        "C00lkidd",
        "John Doe",
        "1x1x1x1",
        "Noli",
    ]

    default = valid_keys

