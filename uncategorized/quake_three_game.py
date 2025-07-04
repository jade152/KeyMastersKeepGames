from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class QuakeThreeArchipelagoOptions:
    quake_three_custom_deathmatch_maps: QuakeThreeCustomDeathmatchMaps
    quake_three_custom_team_deathmatch_maps: QuakeThreeCustomTeamDeathmatchMaps
    quake_three_custom_tournament_maps: QuakeThreeCustomTournamentMaps
    quake_three_custom_ctf_maps: QuakeThreeCustomCTFMaps
    quake_three_custom_characters: QuakeThreeCustomCharacters

class QuakeThreeGame(Game):
    name = "Quake 3 Arena"

    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.DC,
        ]

    is_adult_only_or_unrated = True

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
                    "MAP": (self.maps_ctf, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP with this character present: CHARACTER",
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
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP with this character present: CHARACTER",
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
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP with this character present: CHARACTER",
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
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP with this character present: CHARACTER",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "CHARACTER": (self.characters, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "CHARACTERS": (self.characters, 2)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
                GameObjectiveTemplate(
                label="Win a Free For All game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Team Deathmatch game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Tournament game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
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
                label="Win a Capture The Flag game against COUNT Bots(s) on SKILL in MAP with these characters present: CHARACTERS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "CHARACTERS": (self.characters, 3)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
                ),
            ]

    @functools.cached_property
    def base_maps_deathmatch() -> List[str]:
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

    @functools.cached_property
    def base_maps_team_deathmatch() -> List[str]:
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

    @functools.cached_property
    def base_maps_tournament() -> List[str]:
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

    @functools.cached_property
    def base_maps_ctf() -> List[str]:
        return [
            "Q3CTF1: Dueling Keeps",
            "Q3CTF2: Troubled Waters",
            "Q3CTF3: The Stronghold",
            "Q3CTF4: Space CTF",
            "Q3TOURNEY6_CTF: Across Space",
            ]

    @functools.cached_property
    def base_characters() -> List[str]:
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
            "Grunt",
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

    @property
    def include_custom_deathmatch_maps(self) -> bool:
        return bool(len(self.archipelago_options.quake_three_custom_deathmatch_maps.value) >= 0)

    @property
    def include_custom_team_deathmatch_maps(self) -> bool:
        return bool(len(self.archipelago_options.quake_three_custom_team_deathmatch_maps.value) >= 0)

    @property
    def include_custom_tournament_maps(self) -> bool:
        return bool(len(self.archipelago_options.quake_three_custom_tournament_maps.value) >= 0)

    @property
    def include_custom_ctf_maps(self) -> bool:
        return bool(len(self.archipelago_options.quake_three_custom_ctf_maps.value) >= 0)

    @property
    def include_custom_characters(self) -> bool:
        return bool(len(self.archipelago_options.quake_three_custom_characters.value) >= 0)

    @property
    def custom_maps_ctf(self) -> List[str]:
        return sorted(self.archipelago_options.quake_three_custom_ctf_maps.value)

    @property
    def custom_maps_deathmatch(self) -> List[str]:
        return sorted(self.archipelago_options.quake_three_custom_deathmatch_maps.value)

    @property
    def custom_maps_team_deathmatch(self) -> List[str]:
        return sorted(self.archipelago_options.quake_three_custom_team_deathmatch_maps.value)

    @property
    def custom_maps_tournament(self) -> List[str]:
        return sorted(self.archipelago_options.quake_three_custom_tournament_maps.value)

    @property
    def custom_characters(self) -> List[str]:
        return sorted(self.archipelago_options.quake_three_custom_characters.value)

    def maps_ctf(self) -> List[str]:
        maps: List[str] = self.base_maps_ctf[:]
        if self.include_custom_ctf_maps:
            maps = maps + self.custom_maps_ctf[:]

        return sorted(maps)

    def maps_deathmatch(self) -> List[str]:
        maps: List[str] = self.base_maps_deathmatch[:]
        if self.include_custom_deathmatch_maps:
            maps = maps + self.custom_maps_deathmatch[:]

        return sorted(maps)

    def maps_team_deathmatch(self) -> List[str]:
        maps: List[str] = self.base_maps_team_deathmatch[:]
        if self.include_custom_team_deathmatch_maps:
            maps = maps + self.custom_maps_team_deathmatch[:]

        return sorted(maps)

    def maps_tournament(self) -> List[str]:
        maps: List[str] = self.base_maps_tournament[:]
        if self.include_custom_tournament_maps:
            maps = maps + self.custom_maps_tournament[:]

        return sorted(maps)

    def characters(self) -> List[str]:
        charas: List[str] = self.base_characters[:]
        if self.include_custom_characters:
            charas = charas + self.custom_characters[:]

        return sorted(charas)

# Archipelago Options
# ...
class QuakeThreeCustomDeathmatchMaps(OptionSet):
    """
    Indicates which custom deatmatch maps the player has installed and would like to play on
    """
    display_name = "Custom Free For All Maps"

    default = [
        "Q3DM-Map-1",
        "Q3DM-Map-2",
        "Q3DM-Map-3",
    ]

class QuakeThreeCustomTeamDeathmatchMaps(OptionSet):
    """
    Indicates which custom team deatmatch maps the player has installed and would like to play on
    """
    display_name = "Custom Team Deathmatch Maps"

    default = [
        "Q3DM-Map-1",
        "Q3DM-Map-2",
        "Q3DM-Map-3",
    ]

class QuakeThreeCustomTournamentMaps(OptionSet):
    """
    Indicates which custom tournament maps the player has installed and would like to play on
    """
    display_name = "Custom Tournament Maps"

    default = [
        "Q3DM-Map-1",
        "Q3DM-Map-2",
        "Q3DM-Map-3",
    ]

class QuakeThreeCustomCTFMaps(OptionSet):
    """
    Indicates which custom capture the flag maps the player has installed and would like to play on
    """
    display_name = "Custom Capture The Flag Maps"

    default = [
        "Q3CTF-Map-1",
        "Q3CTF-Map-2",
        "Q3CTF-Map-3",
    ]

class QuakeThreeCustomCharacters(OptionSet):
    """
    Indicates which custom characters the player has installed and would like to play against
    """
    display_name = "Custom Characters"

    default = [
        "Character 1",
        "Character 2",
        "Character 3",
    ]
