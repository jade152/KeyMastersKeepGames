from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class UnrealTournamentArchipelagoOptions:
    unreal_tournament_custom_assault_maps: UnrealTournamentCustomAssaultMaps
    unreal_tournament_custom_ctf_maps: UnrealTournamentCustomCTFMaps
    unreal_tournament_custom_deathmatch_maps: UnrealTournamentCustomDeathmatchMaps
    unreal_tournament_custom_domination_maps: UnrealTournamentCustomDominationhMaps
    unreal_tournament_custom_mutators: UnrealTournamentCustomMutators
    


class UnrealTournamentGame(Game):
    name = "Unreal Tournament: Game of the Year Edition"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.DC,
        KeymastersKeepGamePlatforms.PS2
        ]

    is_adult_only_or_unrated = False

    options_cls = UnrealTournamentArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Game Style: STYLE",
                data={
                    "STYLE": (self.game_styles, 1),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a Deathmatch game against COUNT SKILL Bot(s) in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT SKILL Bot(s) in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT SKILL Bot(s) in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Domination game against COUNT SKILL Bot(s) in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_domination, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win an Assault game against COUNT SKILL Bot(s) in MAP",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_assault, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutator: MUTATOR",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATOR": (self.mutators, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutator: MUTATOR",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATOR": (self.mutators, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT SKILL Bot(s) in MAP with the following Mutator: MUTATOR",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "MUTATOR": (self.mutators, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Domination game against COUNT SKILL Bot(s) in MAP with the following Mutator: MUTATOR",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_domination, 1),
                    "MUTATOR": (self.mutators, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win an Assault game against COUNT SKILL Bot(s) in MAP with the following Mutator: MUTATOR",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_assault, 1),
                    "MUTATOR": (self.mutators, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Domination game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_domination, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win an Assault game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_assault, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATORS": (self.mutators, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Team Deathmatch game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_deathmatch, 1),
                    "MUTATORS": (self.mutators, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Capture The Flag game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_ctf, 1),
                    "MUTATORS": (self.mutators, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Domination game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_domination, 1),
                    "MUTATORS": (self.mutators, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win an Assault game against COUNT SKILL Bot(s) in MAP with the following Mutators: MUTATORS",
                data={
                    "COUNT": (self.bot_count_range, 1),
                    "SKILL": (self.bot_skill_levels, 1),
                    "MAP": (self.maps_assault, 1),
                    "MUTATORS": (self.mutators, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

    @functools.cached_property
    def base_maps_assault(self) -> List[str]:
        return [
            "AS-Frigate",
            "AS-Guardia",
            "AS-HiSpeed",
            "AS-Mazon",
            "AS-OceanFloor",
            "AS-Overlord",
            "AS-Rook",
        ]

    @functools.cached_property
    def base_maps_ctf(self) -> List[str]:
        return [
            "CTF-Command",
            "CTF-Coret",
            "CTF-Dreart",
            "CTF-EternalCave",
            "CTF-Face",
            "CTF-Gauntlet",
            "CTF-LavaGiant",
            "CTF-Niven",
            "CTF-November",
            "CTF-Cybrosis][",
            "CTF-Darji16",
            "CTF-Hydro16",
            "CTF-Noxion16",
            "CTF-HallOfGiants",
            "CTF-Face][",
            "CTF-High",
            "CTF-Kosov",
            "CTF-Nucleus",
        ]

    @functools.cached_property
    def base_maps_deathmatch(self) -> List[str]:
        return [
            "DM-Barricade",
            "DM-Codex",
            "DM-Conveyor",
            "DM-Curse][",
            "DM-Deck16][",
            "DM-Fetid",
            "DM-Fractal",
            "DM-Gothic",
            "DM-Grinder",
            "DM-HyperBlast",
            "DM-KGalleon",
            "DM-Liandri",
            "DM-Morbias][",
            "DM-Morpheus",
            "DM-Oblivion",
            "DM-Peak",
            "DM-Phobos",
            "DM-Pressure",
            "DM-Pyramid",
            "DM-Stalwart",
            "DM-StalwartXL",
            "DM-Tempest",
            "DM-Turbine",
            "DM-Zeto",
            "DM-Agony",
            "DM-ArcaneTemple",
            "DM-Cybrosis][",
            "DM-HealPod][",
            "DM-Malevolence",
            "DM-Mojo][",
            "DM-Shrapnel][",
            "DM-Crane",
            "DM-SpaceNoxx",
        ]

    @functools.cached_property
    def base_maps_domination(self) -> List[str]:
        return [
            "DOM-Cinder",
            "DOM-Condemned",
            "DOM-Cryptic",
            "DOM-Gearbolt",
            "DOM-Ghardhen",
            "DOM-Lament",
            "DOM-Leadworks",
            "DOM-MetalDream",
            "DOM-Olden",
            "DOM-Sesmar",
        ]

    @staticmethod
    def bot_skill_levels() -> List[str]:
        return [
            "Novice",
            "Average",
            "Experienced",
            "Skilled",
            "Adept",
            "Masterful",
            "Inhuman",
            "Godlike",
        ]

    @functools.cached_property
    def base_mutators(self) -> List[str]:
        return [
            "Flak Cannon Arena",
            "Pulse Arena",
            "Rocket Launcher Arena",
            "Shock Rifle Arena",
            "Sniper Rifle Arena",
            "Chainsaw Melee",
            "FatBoy",
            "Instagib DM",
            "Instant Rockets",
            "Impact Hammer Arena",
            "Minigun Arena",
            "Jump Match",
            "Low Gravity",
            "No Powerups",
            "No Redeemer",
            "Relic: Defense",
            "Relic: Redemption",
            "Relic: Regen",
            "Relic: Speed",
            "Relic: Strength",
            "Relic: Vengeance",
            "Stealth",
            "Team Beacon",
            "Volatile Ammo",
            "Volatile Weapon",
        ]

    @staticmethod
    def bot_count_range() -> range:
        return range(1, 16)

    @staticmethod
    def game_styles() -> List[str]:
        return [
            "Classic",
            "Hardcore",
            "Turbo",
        ]

    @property
    def include_custom_assault_maps(self) -> bool:
        return bool(len(self.archipelago_options.unreal_tournament_custom_assault_maps.value) >= 0)

    @property
    def include_custom_ctf_maps(self) -> bool:
        return bool(len(self.archipelago_options.unreal_tournament_custom_ctf_maps.value) >= 0)
    
    @property
    def include_custom_deathmatch_maps(self) -> bool:
        return bool(len(self.archipelago_options.unreal_tournament_custom_deathmatch_maps.value) >= 0)
    
    @property
    def include_custom_domination_maps(self) -> bool:
        return bool(len(self.archipelago_options.unreal_tournament_custom_domination_maps.value) >= 0)

    @property
    def include_custom_mutators(self) -> bool:
        return bool(len(self.archipelago_options.unreal_tournament_custom_mutators.value) >= 0)
    
    @property
    def custom_maps_assault(self) -> List[str]:
        return sorted(self.archipelago_options.unreal_tournament_custom_assault_maps.value)
    
    @property
    def custom_maps_ctf(self) -> List[str]:
        return sorted(self.archipelago_options.unreal_tournament_custom_ctf_maps.value)
    
    @property
    def custom_maps_deathmatch(self) -> List[str]:
        return sorted(self.archipelago_options.unreal_tournament_custom_deathmatch_maps.value)
    
    @property
    def custom_maps_domination(self) -> List[str]:
        return sorted(self.archipelago_options.unreal_tournament_custom_domination_maps.value)

    @property
    def custom_mutators(self) -> List[str]:
        return sorted(self.archipelago_options.unreal_tournament_custom_mutators)


    def maps_assault(self) -> List[str]:
        maps: List[str] = self.base_maps_assault[:]
        if self.include_custom_assault_maps:
            maps = maps + self.custom_maps_assault[:]
        
        return sorted(maps)

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

    def maps_domination(self) -> List[str]:
        maps: List[str] = self.base_maps_ctf[:]
        if self.include_custom_domination_maps:
            maps = maps + self.custom_maps_domination[:]
        
        return sorted(maps)

    def mutators(self) -> List[str]:
        mutators: List[str] = self.base_mutators[:]
        if self.include_custom_mutators:
            mutators = mutators + self.custom_mutators[:]
        
        return sorted(mutators)


# Archipelago Options
# ...
class UnrealTournamentCustomAssaultMaps(OptionSet):
    """
    Indicates custom Assault maps the player has installed and want to possibly play on 
    """
    display_name = "Custom Assault Maps"

    default = [
        "AS-Map",
        "AS-Map][",
        "AS-Map3",
    ]

class UnrealTournamentCustomCTFMaps(OptionSet):
    """
    Indicates custom Capture The Flag maps the player has installed and want to possibly play on 
    """
    display_name = "Custom Capture The Flag Maps"

    default = [
        "CTF-Map",
        "CTF-Map][",
        "CTF-Map3",
    ]

class UnrealTournamentCustomDeathmatchMaps(OptionSet):
    """
    Indicates custom Deathmatch maps the player has installed and want to possibly play on 
    """
    display_name = "Custom Deathmatch Maps"

    default = [
        "DM-Map",
        "DM-Map][",
        "DM-Map3",
    ]

class UnrealTournamentCustomDominationhMaps(OptionSet):
    """
    Indicates custom Domination maps the player has installed and want to possibly play on 
    """
    display_name = "Custom Domination Maps"

    default = [
        "DOM-Map",
        "DOM-Map][",
        "DOM-Map3",
    ]

class UnrealTournamentCustomMutators(OptionSet):
    """
    Indicates custom Mutators the player has installed and want to possibly activate
    """
    display_name = "Custom Mutators"
    default = [
        "Mutator 1",
        "Mutator 2",
        "Mutator 3"
    ]