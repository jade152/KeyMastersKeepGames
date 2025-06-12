from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class DandysWorldGameArchipelagoOptions:
    dandys_characters_owned: DandysCharactersOwned
    dandys_trinkets_owned: DandysTrinketsOwned


class DandysWorldGame(Game):
    name = "Dandy's World (Roblox)"

    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
    ]

    is_adult_only_or_unrated = False

    options_cls = DandysWorldGameArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Reach floor COUNT",
                data={
                    "COUNT": (self.floor_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Reach floor COUNT with CHARACTER",
                data={
                    "COUNT": (self.floor_range, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Reach floor COUNT with TRINKET equipped",
                data={
                    "COUNT": (self.floor_range, 1),
                    "TRINKET": (self.trinkets, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Reach floor COUNT with TRINKET equipped as CHARACTER",
                data={
                    "COUNT": (self.floor_range, 1),
                    "TRINKET": (self.trinkets, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Pick up COUNT items in a floor",
                data={
                    "COUNT": (self.item_count_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Pick up COUNT tapes in a floor",
                data={
                    "COUNT": (self.item_count_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete COUNT skill checks in a floor",
                data={
                    "COUNT": (self.skill_check_count_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with a Common Twisted",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with an Uncommon Twisted",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with a Rare Twisted",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with COUNT Common Twisteds",
                data={
                    "COUNT": (self.twisted_count_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with COUNT Uncommon Twisteds",
                data={
                    "COUNT": (self.twisted_count_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with COUNT Rare Twisteds",
                data={
                    "COUNT": (self.twisted_count_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Have your items stolen by Twisted Gigi",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Encounter a Twisted Main Character",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach floor 10",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach floor 10 as CHARACTER",
                data={
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach floor 10 with TRINKET equipped",
                data={
                    "TRINKET": (self.trinkets, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach floor 10 with TRINKET equipped as CHARACTER",
                data={
                    "TRINKET": (self.trinkets, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Encounter Twisted Dandy",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Survive a floor with Twisted Dandy",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Pick up every item on the floor",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def floor_range() -> range:
        return range(1, 9)
    
    @staticmethod
    def twisted_count_range() -> range:
        return range(1, 6)
    
    @staticmethod
    def skill_check_count_range() -> range:
        return range(1, 6)
    
    @staticmethod
    def item_count_range() -> range:
        return range(1, 10)
    
    def characters(self) -> List[str]:
        return sorted(self.archipelago_options.dandys_characters_owned)
    
    def trinkets(self) -> List[str]:
        return sorted(self.archipelago_options.dandys_trinkets_owned)

class DandysCharactersOwned(OptionSet):
    """
    Indicates which characters the player owns and wants to possibly play as.
    """
    display_name = "Dandy's World Toons Owned"
    valid_keys = [
        "Blot",
        "Boxten",
        "Brightney",
        "Connie",
        "Cosmo",
        "Finn",
        "Flutter",
        "Gigi",
        "Glisten",
        "Goob",
        "Looey",
        "Poppy",
        "Razzle & Dazzle",
        "Rodger",
        "Scraps",
        "Shrimpo",
        "Teagan",
        "Tisha",
        "Toodles",
        "Yatta",
        "Astro",
        "Bassie",
        "Bobette",
        "Pebble",
        "Shelly",
        "Sprout",
        "Vee",
        "Bassie",
        "Cocoa",
        "Eggson",
        "Flyte",
        "Bobette",
        "Coal",
        "Ginger",
        "Rudie",
    ]

    default = valid_keys

class DandysTrinketsOwned(OptionSet):
    """
    Indicates which trinkets the player owns and wants to possibly play as.
    """
    display_name = "Dandy's World Trinkets Owned"
    valid_keys = [
        "Alarm",
        "Blushy Bat",
        "Cardboard 'Armor'",
        "Coin Purse",
        "Machine Manual",
        "Megaphone",
        "Pop Pack",
        "Pull Toy",
        "Speedometer",
        "Speedy Shoes",
        "Thermos",
        "Thinking Cap",
        "Water Cooler",
        "Wrench",
        "Blue Bandana",
        "Brick",
        "Clown Horn",
        "Feather Duster",
        "Party Popper",
        "Pink Bow",
        "Sweet Charm",
        "Dog Plush",
        "Fancy Purse",
        "Fishing Rod",
        "Ghost Snakes In A Can",
        "Magnifying Glass",
        "Ribbon Spool",
        "Spare Bulb",
        "Crayon Set",
        "Diary",
        "Friendship Bracelet",
        "Lucky Coin",
        "Mime Makeup",
        "Vanity Mirror",
        "Bone",
        "Participation Award",
        "Savory Charm",
        "Star Pillow",
        "Vee's Remote",
        "Dandy Plush",
        "Coal (Trinket)",
        "Egg Radar",
        "Festive Lights",
        "Glazed Fondant Bag",
        "Peppermint Icing",
        "Scrapbook",
        "Toy Kit",
        "Whispering Flower",
    ]

    default = valid_keys