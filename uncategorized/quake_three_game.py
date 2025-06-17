from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class QuakeThreeArchipelagoOptions:
    pass

class QuakeThreeGame(Game):
    name = "Quake 3 Arena"

    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.DC,
        ]

    is_adult_only_or_unrated = False

    options_cls = QuakeThreeArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Obtain a MEDAL medal in this keep",
                data={
                    "MEDAL": (self.medals, 1),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
         return [
             GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
                ),
                GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_team_deathmatch, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
                ),
                GameObjectiveTemplate(
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP against the following character: CHARACTER",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "CHARACTER": (self.characters, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP against the following character: CHARACTER",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_team_deathmatch, 1),
                    "CHARACTER": (self.characters, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP against the following character: CHARACTER",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTER": (self.characters, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP against the following character: CHARACTER",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTER": (self.characters, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "CHARACTERS": (self.characters, 2)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_team_deathmatch, 1),
                    "CHARACTERS": (self.characters, 2)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTERS": (self.characters, 2)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTERS": (self.characters, 2)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "CHARACTERS": (self.characters, 3)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_team_deathmatch, 1),
                    "CHARACTERS": (self.characters, 3)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTERS": (self.characters, 3)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP against the following characters: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_tournament, 1),
                    "CHARACTERS": (self.characters, 3)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
            ]

    @staticmethod
    def game_types() -> List[str]:
        return [
            "Free For All",
            "Team Deathmatch",
            "Tournament",
            "Capture The Flag",
            ]

    @staticmethod
    def maps_deathmatch() -> List[str]:
        return [
        "Q3DM10: The Nameless Place",
        "Q3DM11: Deva Station",
        "Q3DM12: The Dredwerkz",
        "Q3DM13: Lost World",
        "Q3DM14: Grim Dungeons",
        "Q3DM15: Demon Keep",
        "Q3DM16: Bouncy Map",
        "Q3DM17: The Longest Yard",
        "Q3DM18: Space Chamber",
        "Q3DM19: Apocalypse Void",
        "Q3DM1: Arena Gate",
        "Q3DM2: House of Pain",
        "Q3DM3: Arena of Death",
        "Q3DM4: The Place of Many Deaths",
        "Q3DM5: The Forgotten Place",
        "Q3DM6: The Camping Grounds",
        "Q3DM7: Temple of Retribution",
        "Q3DM8: Brimstone Abbey",
        "Q3DM9: Hero\'s Keep",
        "Q3TOURNEY1: Powerstation 0218",
        "Q3TOURNEY2: The Proving Grounds",
        "Q3TOURNEY3: Hell\'s Gate",
        "Q3TOURNEY4: Vertical Vengeance",
        "Q3TOURNEY5: Fatal Instinct",
        "Q3TOURNEY6: The Very End of You",
        "PRO-Q3TOURNEY8: Dark Reign",
        "PRO_Q3DM6: The Campgrounds II",
        "PRO_Q3DM13: Lost World II",
        "PRO_Q3TOURNEY2: The Proving Grounds II",
        "PRO_Q3TOURNEY4: Vertical Vengeance II",
        ]

    @staticmethod
    def maps_team_deathmatch() -> List[str]:
        return [
        "Q3DM12: The Dredwerkz",
        "Q3DM14: Grim Dungeons",
        "Q3DM15: Demon Keep",
        "Q3DM6: The Camping Grounds",
        "Q3DM7: Temple of Retribution",
        "Q3DM8: Brimstone Abbey",
        "Q3DM9: Hero\'s Keep",
        "Q3TOURNEY2: The Proving Grounds",
        "Q3TOURNEY4: Vertical Vengeance",
        "PRO_Q3DM6: The Campgrounds II",
        "PRO_Q3DM13: Lost World II",
        ]

    @staticmethod
    def maps_tournament() -> List[str]:
        return [
            "Q3DM1: Arena Gate",
            "Q3DM2: House of Pain",
            "Q3TOURNEY1: Powerstation 0218",
            "Q3TOURNEY2: The Proving Grounds",
            "Q3TOURNEY3: Hell\'s Gate",
            "Q3TOURNEY4: Vertical Vengeance",
            "PRO_Q3DM6: The Campgrounds II",
            "PRO_Q3DM13: Lost World II",
            ]

    @staticmethod
    def maps_ctf() -> List[str]:
        return [
            "Q3CTF1: Dueling Keeps",
            "Q3CTF2: Troubled Waters",
            "Q3CTF3: The Stronghold",
            "Q3CTF4: Space CTF",
            "Q3TOURNEY6_CTF: Across Space",
            ]

    @staticmethod
    def characters() -> List[str]:
        return [
            "Anarki",
            "Angel",
            "Biker",
            "Bitterman",
            "Bones",
            "Cadaver",
            "Crash",
            "Daemia",
            "Doom",
            "Gorre",
            "Grun",
            "Hossman",
            "Hunter",
            "Keel",
            "Klesk",
            "Lucy",
            "Major",
            "Mynx",
            "Orbb",
            "Patriot",
            "Phobos",
            "Ranger",
            "Razor",
            "Sarge",
            "Slash",
            "Sorlag"
            "Stripe",
            "Tank Jr.",
            "Uriel"
            "Visor",
            "Wrack",
            "Xaero",
            ]

    @staticmethod
    def skill_levels() -> List[str]:
        return [
            "I Can Win",
            "Bring It On",
            "Hurt Me Plenty",
            "Hardcore",
            "Nightmare!",
            ]

    @staticmethod
    def bot_count_range() -> range:
        return range(1, 11)

    @staticmethod
    def medals() -> List[str]:
        return [
            "Excellent",
            "Impressive",
            "Gauntlet",
            ]

# Archipelago Options
# ...

