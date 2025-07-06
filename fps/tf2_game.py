from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class TF2ArchipelagoOptions:
    tf2_halloween: TF2Halloween
    tf2_smissmas: TF2Smissmas
    tf2_mvm: TF2MVM
    tf2_alternative_gamemodes: TF2AlternativeGamemodes
    tf2_owned_scout_primaries: TF2OwnedScoutPrimaries
    tf2_owned_scout_secondaries: TF2OwnedScoutSecondaries
    tf2_owned_scout_melees: TF2OwnedScoutMelees
    tf2_owned_soldier_primaries: TF2OwnedSoldierPrimaries
    tf2_owned_soldier_secondaries: TF2OwnedSoldierSecondaries
    tf2_owned_soldier_melees: TF2OwnedSoldierMelees
    tf2_owned_pyro_primaries: TF2OwnedPyroPrimaries
    tf2_owned_pyro_secondaries: TF2OwnedPyroSecondaries
    tf2_owned_pyro_melees: TF2OwnedPyroMelees
    tf2_owned_demoman_primaries: TF2OwnedDemomanPrimaries
    tf2_owned_demoman_secondaries: TF2OwnedDemomanSecondaries
    tf2_owned_demoman_melees: TF2OwnedDemomanMelees
    tf2_owned_engineer_primaries: TF2OwnedEngineerPrimaries
    tf2_owned_engineer_secondaries: TF2OwnedEngineerSecondaries
    tf2_owned_engineer_melees: TF2OwnedEngineerMelees
    tf2_owned_heavy_primaries: TF2OwnedHeavyPrimaries
    tf2_owned_heavy_secondaries: TF2OwnedHeavySecondaries
    tf2_owned_heavy_melees: TF2OwnedHeavyMelees
    tf2_owned_medic_primaries: TF2OwnedMedicPrimaries
    tf2_owned_medic_secondaries: TF2OwnedMedicSecondaries
    tf2_owned_medic_melees: TF2OwnedMedicMelees
    tf2_owned_sniper_primaries: TF2OwnedSniperPrimaries
    tf2_owned_sniper_secondaries: TF2OwnedSniperSecondaries
    tf2_owned_sniper_melees: TF2OwnedSniperMelees
    tf2_owned_spy_watches: TF2OwnedSpyWatches
    tf2_owned_spy_secondaries: TF2OwnedSpySecondaries
    tf2_owned_spy_buildings: TF2OwnedSpyBuildings
    tf2_owned_spy_melees: TF2OwnedSpyMelees

class TF2Game(Game):
    name = "Team Fortress 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.X360,
        KeymastersKeepGamePlatforms.PS3,
        ]

    is_adult_only_or_unrated = True

    options_cls = TF2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Win an Attack/Defense game on MAP",
                data={
                    "MAP": (self.maps_ad, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a Capture The Flag game on MAP",
                data={
                    "MAP": (self.maps_ctf, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a Control Points game on MAP",
                data={
                    "MAP": (self.maps_cp, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a King of the Hill game on MAP",
                data={
                    "MAP": (self.maps_koth, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a Payload game on MAP",
                data={
                    "MAP": (self.maps_pl, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a game as CLASS",
                data={
                    "MAP": (self.classes, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Scout loadout: SCOUTPRIMARY, SCOUTSECONDARY, SCOUTMELEE",
                data={
                    "SCOUTPRIMARY": (self.scout_primaries, 1),
                    "SCOUTSECONDARY": (self.scout_secondaries, 1),
                    "SCOUTMELEE": (self.scout_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Soldier loadout: SOLDIERPRIMARY, SOLDIERSECONDARY, SOLDIERMELEE",
                data={
                    "SOLDIERPRIMARY": (self.soldier_primaries, 1),
                    "SOLDIERSECONDARY": (self.soldier_secondaries, 1),
                    "SOLDIERMELEE": (self.soldier_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Pyro loadout: PYROPRIMARY, PYROSECONDARY, PYROMELEE",
                data={
                    "PYROPRIMARY": (self.pyro_primaries, 1),
                    "PYROSECONDARY": (self.pyro_secondaries, 1),
                    "PYROMELEE": (self.pyro_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Demoman loadout: DEMOMANPRIMARY, DEMOMANSECONDARY, DEMOMANMELEE",
                data={
                    "DEMOMANPRIMARY": (self.demoman_primaries, 1),
                    "DEMOMANSECONDARY": (self.demoman_secondaries, 1),
                    "DEMOMANMELEE": (self.demoman_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Engineer loadout: ENGINEERPRIMARY, ENGINEERSECONDARY, ENGINEERMELEE",
                data={
                    "ENGINEERPRIMARY": (self.engineer_primaries, 1),
                    "ENGINEERSECONDARY": (self.engineer_secondaries, 1),
                    "ENGINEERMELEE": (self.engineer_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Heavy loadout: HEAVYPRIMARY, HEAVYSECONDARY, HEAVYMELEE",
                data={
                    "HEAVYPRIMARY": (self.heavy_primaries, 1),
                    "HEAVYSECONDARY": (self.heavy_secondaries, 1),
                    "HEAVYMELEE": (self.heavy_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Medic loadout: MEDICPRIMARY, MEDICSECONDARY, MEDICMELEE",
                data={
                    "MEDICPRIMARY": (self.medic_primaries, 1),
                    "MEDICSECONDARY": (self.medic_secondaries, 1),
                    "MEDICMELEE": (self.medic_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Sniper loadout: SNIPER_PRIMARY, SNIPER_SECONDARY, SNIPER_MELEE",
                data={
                    "SNIPER_PRIMARY": (self.sniper_primaries, 1),
                    "SNIPER_SECONDARY": (self.sniper_secondaries, 1),
                    "SNIPER_MELEE": (self.sniper_melees, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game with the following Spy loadout: SPYWATCH, SPYSECONDARY, SPYMELEE, SPYBUILDING",
                data={
                    "SPYWATCH": (self.spy_watches, 1),
                    "SPYSECONDARY": (self.spy_secondaries, 1),
                    "SPYMELEE": (self.spy_melees, 1),
                    "SPYBUILDING": (self.spy_buildings, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ])

        

        if self.include_alternative_gamemodes:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Win a Payload Race game on MAP",
                    data={
                        "MAP": (self.maps_plr, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Win a Mannpower game on MAP",
                    data={
                        "MAP": (self.maps_mannpower, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Win a Pass Time game on MAP",
                    data={
                        "MAP": (self.maps_pass, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Win a Special Delivery game on MAP",
                    data={
                        "MAP": (self.maps_sd, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Win a Territorial Control game on MAP",
                    data={
                        "MAP": (self.maps_tc, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Win a Versus Saxton Hale game on MAP",
                    data={
                        "MAP": (self.maps_vsh, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Win a Medival Mode game on MAP",
                    data={
                        "MAP": (self.maps_medival, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
            ])

        if self.include_mvm:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Win a Mann Vs Machine Mission on MAP",
                    data={
                        "MAP": (self.maps_mvm, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])

        return game_objective_templates

    @functools.cached_property
    def base_maps_ctf(self) -> List[str]:
        return [
            "2Fort",
            "2Fort Invasion",
            "Applejack",
            "Double Cross",
            "Frosty",
            "Landfall",
            "Pelican Peak",
            "Penguin Peak",
            "Sawmil",
            "Turbine",
            "Well"
            ]

    @functools.cached_property
    def halloween_maps_ctf(self) -> List[str]:
        return [
            "Crasher",
            "Helltrain",
            ]

    @functools.cached_property
    def smissmas_maps_ctf(self) -> List[str]:
        return [
            "Snowfall",
            ]

    @functools.cached_property
    def base_maps_cp(self) -> List[str]:
        return [
            "5Gorge",
            "Badlands",
            "Canaveral",
            "Coldfront",
            "Fastlane",
            "Foundry",
            "Frieght",
            "Granary",
            "Gullywash",
            "Metalworks",
            "Powerhouse",
            "Process",
            "Reckoner",
            "Snakewater",
            "Standin",
            "Sunshine",
            "Vanguard",
            "Well",
            "Yukon",
            ]

    @functools.cached_property
    def halloween_maps_cp(self) -> List[str]:
        return [
            "Freaky Fair",
            "Sinshine",
            ]

    @functools.cached_property
    def base_maps_ad(self) -> List[str]:
        return [
            "Altitude",
            "Brew",
            "Dustbowl",
            "Egypt",
            "Fortezza",
            "Gorge",
            "Gravelpit",
            "Haarp",
            "Hadal",
            "Hardwood",
            "Junction",
            "Mercenary Park",
            "Mossrock",
            "Mountain Lab",
            "Overgrown",
            "Snowplow",
            "Steel",
            "Sulfur"
            ]

    @functools.cached_property
    def medival_maps_ad(self) -> List[str]:
        return [
            "Burghausen",
            "DeGroot Keep",
            ]

    @functools.cached_property
    def halloween_medival_maps_ad(self) -> List[str]:
        return [
            "Sandcastle",
            ]

    @functools.cached_property
    def base_maps_koth(self) -> List[str]:
        return [
            "Badlands",
            "Brazil",
            "Cachoeria",
            "Cascade",
            "Harvest",
            "Highpass",
            "Kong King",
            "Lakeside",
            "Lazarus",
            "Megaton",
            "Nucleus",
            "Overcast",
            "Probed",
            "Rotunda",
            "Sawmil",
            "Sharkbay",
            "Snowtower",
            "Suijin",
            "Viaduct",
            ]

    @functools.cached_property
    def halloween_maps_koth(self) -> List[str]:
        return [
            "Harvest Event",
            "Krampus",
            "Laughter",
            "Los Muertos",
            "Maple Ridge Event",
            "Megalo",
            "Moldergrove",
            "Moonshine Event",
            "Sinthetic",
            "Slasher",
            "Slime",
            "Soul-Mill",
            "Toxic",
            "Cauldron",
            "Eyeaduct",
            "Ghost Fort",
            ]

    @functools.cached_property
    def base_maps_pl(self) -> List[str]:
        return [
            "Badwater",
            "Barnblitz",
            "Borneo",
            "Bread Space",
            "Camber",
            "Cashworks",
            "Embargo",
            "Emerge",
            "Enclosure",
            "Frontier",
            "Goldrush",
            "Hoodoo",
            "Odyssey",
            "Patagonia",
            "Phoenix",
            "Pier",
            "Rumford",
            "Snowycoast",
            "Swiftwater",
            "Thundermountain",
            "Upward",
            "Venice"
            ]

    @functools.cached_property
    def halloween_maps_pl(self) -> List[str]:
        return [
            "Corruption",
            "Ghoulpit",
            "Gravestone",
            "Hassle Castle",
            "Hellstone",
            "Precipice",
            "Spineyard",
            "Terror",
            ]

    @functools.cached_property
    def smissmas_maps_pl(self) -> List[str]:
        return [
            "Chilly",
            "Frostcliff",
            "Polar",
            ]

    @functools.cached_property
    def base_maps_plr(self) -> List[str]:
        return [
            "Banana Bay",
            "Hacksaw",
            "Hightower",
            "Nightfall",
            "Pipeline",
            ]

    @functools.cached_property
    def halloween_maps_plr(self) -> List[str]:
        return [
            "Bonesaw",
            "Cutter",
            "Helltower",
            ]

    @functools.cached_property
    def base_maps_pass(self) -> List[str]:
        return [
            "Brickyard",
            "District",
            "Timbertown",
            ]

    @functools.cached_property
    def base_maps_mvm(self) -> List[str]:
        return [
            "Bigrock",
            "Coal Town",
            "Decoy",
            "Ghost Town",
            "Mannhattan",
            "Mannworks",
            "Rottenburg",
            ]

    @functools.cached_property
    def base_maps_ctf_mannpower(self) -> List[str]:
        return [
            "Foundry",
            "Gorge",
            "Hellfire",
            "Thundermountain",
            ]

    @functools.cached_property
    def base_maps_pd(self) -> List[str]:
        return [
            "Atom Smash",
            "Watergate",
            "Selbyen"
            ]

    @functools.cached_property
    def halloween_maps_pd(self) -> List[str]:
        return [
            "Circus",
            "Cursed Cove",
            "Farmageddon",
            "Galleria",
            "Mannsylvania",
            "Monster Bash",
            "Pit of Death",
            ]

    @functools.cached_property
    def smissmas_maps_pd(self) -> List[str]:
        return [
            "SnowVille",
            ]

    @functools.cached_property
    def base_maps_sd(self) -> List[str]:
        return [
            "Doomsday",
            ]

    @functools.cached_property
    def halloween_maps_sd(self) -> List[str]:
        return [
            "Carnival of Carnage",
            ]

    @functools.cached_property
    def base_maps_tc(self) -> List[str]:
        return [
            "Hydro",
            ]

    @functools.cached_property
    def halloween_maps_tow(self) -> List[str]:
        return [
            "Dynamite"
            ]

    @functools.cached_property
    def base_maps_vsh(self) -> List[str]:
        return [
            "Distillery",
            "Nucleus VSH",
            "Skirmish",
            "Tiny Rock",
            ]

    @functools.cached_property
    def smissmas_maps_vsh(self) -> List[str]:
        return [
            "Maul",
            ]

    @functools.cached_property
    def halloween_maps_vsh(self) -> List[str]:
        return [
            "Outburst",
            ]

    @functools.cached_property
    def halloween_maps_zi(self) -> List[str]:
        return [
            "Atoll",
            "Blazehattan",
            "Devasation",
            "Murky",
            "Sanitarium",
            "Woods",
            ]

    @functools.cached_property
    def all_scout_primaries(self) -> List[str]:
        return [
            "Scattergun",
            "Force-A-Nature",
            "Shortstop",
            "Soda Popper",
            "Baby Face\'s Blaster",
            "Back Scatter",
            ]

    @functools.cached_property
    def all_scout_secondaries(self) -> List[str]:
        return [
            "Pistol",
            "Lugermorph",
            "C.A.P.P.E.R",
            "Winger",
            "Pretty Boy\'s Pocket Pistol",
            "Flying Guillotine",
            "Bonk! Atomic Punch",
            "Crit-a-Cola",
            "Mad Milk",
            "Mutated Milk",
            ]

    @functools.cached_property
    def all_scout_melees(self) -> List[str]:
        return [
            "Bat",
            "Holy Mackerel",
            "Unarmed Combat",
            "Batsaber",
            "Sandman",
            "Candy Cane",
            "Boston Basher",
            "Three-Rune Blade",
            "Sun-on-a-Stick",
            "Fan O\'War",
            "Atomizer",
            "Wrap Assasin",
            ]

    @functools.cached_property
    def all_soldier_primaries(self) -> List[str]:
        return [
            "Rocket Launcher",
            "Original",
            "Direct Hit",
            "Black Box",
            "Rocket Jumper",
            "Liberty Launcher",
            "Cow Mangler 5000",
            "Beggar\'s Bazooka",
            "Air Strike",
            ]

    @functools.cached_property
    def all_soldier_secondaries(self) -> List[str]:
        return [
            "Shotgun",
            "Reserve Shooter",
            "Buff Banner",
            "Gunboats",
            "Battalion\'s Backup",
            "Concheror",
            "Mantreads",
            "Righteous Bison",
            "B.A.S.E. Jumper",
            "Panic Attack",
            ]

    @functools.cached_property
    def all_soldier_melees(self) -> List[str]:
        return [
            "Shovel",
            "Equalizer",
            "Pain Train",
            "Half-Zatoichi",
            "Disciplinary Action",
            "Market Gardener",
            "Escape Plan",
            "Panic Attack",
            ]

    @functools.cached_property
    def all_pyro_primaries(self) -> List[str]:
        return [
            "Flame Thrower",
            "Rainblower",
            "Nostromo Napalmer",
            "Backburner",
            "Degreaser",
            "Phlogistinator",
            "Dragon\'s Fury",
            ]

    @functools.cached_property
    def all_pyro_secondaries(self) -> List[str]:
        return [
            "Shotgun",
            "Reserve Shooter",
            "Panic Attack",
            "Flare Gun",
            "Detonator",
            "Manmelter",
            "Scortch Shot",
            "Thermal Thruster",
            "Gas Passer",
            ]

    @functools.cached_property
    def all_pyro_melees(self) -> List[str]:
        return [
            "Fire Axe",
            "Lollichop",
            "Axtinguisher",
            "Postal Pummeler",
            "Homewrecker",
            "Maul",
            "Powerjack",
            "Back Scratcher",
            "Sharpened Volcano Fragment",
            "Third Degree",
            "Neon Annihilator",
            "Hot Hand",
            ]

    @functools.cached_property
    def all_demoman_primaries(self) -> List[str]:
        return [
            "Grenade Launcher",
            "Loch-n-Load",
            "Ali Baba\'s Wee Booties",
            "Bootlegger",
            "Loose Cannon",
            "Iron Bomber",
            "B.A.S.E. Jumper",
            ]

    @functools.cached_property
    def all_demoman_secondaries(self) -> List[str]:
        return [
            "Stickybomb Launcher",
            "Scottish Resistance",
            "Chargnin' Targe",
            "Sticky Jumper",
            "Splendid Screen",
            "Tide Turner",
            "Quickebomb Launcher",
            ]

    @functools.cached_property
    def all_demoman_melees(self) -> List[str]:
        return [
            "Bottle",
            "Scottish Handshake",
            "Eyelander",
            "Horseless Headless Horsemann\'s Headtaker",
            "Nessie\'s Nine Iron",
            "Scotsman\'s Skullcutter",
            "Pain Train",
            "Ullapool Caber",
            "Claidheamh Mòr",
            "Half-Zatoichi",
            "Persian Persuader",
            ]

    @functools.cached_property
    def all_engineer_primaries(self) -> List[str]:
        return [
            "Shotgun",
            "Frontier Justice",
            "Widowmaker",
            "Pomson 6000",
            "Rescue Ranger",
            "Panic Attack",
            ]

    @functools.cached_property
    def all_engineer_secondaries(self) -> List[str]:
        return [
            "Pistol",
            "Lugermorph",
            "C.A.P.P.E.R",
            "Wrangler",
            "Giger Counter",
            "Short Circut",
            ]

    @functools.cached_property
    def all_engineer_melees(self) -> List[str]:
        return [
            "Wrench",
            "Gunslinger",
            "Souther Hospitality",
            "Jag",
            "Eureka Effect",
            ]

    @functools.cached_property
    def all_heavy_primaries(self) -> List[str]:
        return [
            "Minigun",
            "Iron Curtain",
            "Natasha",
            "Brass Beast",
            "Tomislav",
            "Huo-Long Heater",
            ]

    @functools.cached_property
    def all_heavy_secondaries(self) -> List[str]:
        return [
            "Shotgun",
            "Family Buisness",
            "Sandvich",
            "Robo-Sandvich",
            "Dalokohs Bar",
            "Fishcake",
            "Buffalo Steak Sandvich",
            "Panic Attack",
            "Second Banana",
            ]

    @functools.cached_property
    def all_heavy_melees(self) -> List[str]:
        return [
            "Fists",
            "Apoco-Fists",
            "Killing Gloves of Boxing",
            "Gloves of Running Urgently",
            "Bread Bite",
            "Warrior\'s Spirit",
            "Fists of Steel",
            "Eviction Notice",
            "Holiday Punch",
            ]

    @functools.cached_property
    def all_medic_primaries(self) -> List[str]:
        return [
            "Syringe Gun",
            "Blutsauger",
            "Crusader\'s Crossbow",
            "Overdose",
            ]

    @functools.cached_property
    def all_medic_secondaries(self) -> List[str]:
        return [
            "Medi Gun",
            "Kritzkrieg",
            "Quick-Fix",
            "Vaccinator",
            ]

    @functools.cached_property
    def all_medic_melees(self) -> List[str]:
        return [
            "Bonesaw",
            "Ubersaw",
            "Vita-Saw",
            "Amputator",
            "Solemm Vow",
            ]

    @functools.cached_property
    def all_sniper_primaries(self) -> List[str]:
        return [
            "Sniper Rifle",
            "AWPer Hand",
            "Huntsman",
            "Fortified Compound",
            "Sydney Sleeper",
            "Bazaar Bargain",
            "Machina",
            "Shooting Star",
            "Hitman\'s Heatmaker",
            "Classic",
            ]

    @functools.cached_property
    def all_sniper_secondaries(self) -> List[str]:
        return [
            "SMG",
            "Cleaner\'s Carbine",
            "Jarate",
            "Self-Aware Beauty Mark",
            "Razorback",
            "Darwin\'s Danger Shield",
            "Cozy Camper",
            ]

    @functools.cached_property
    def all_sniper_melees(self) -> List[str]:
        return [
            "Kukri",
            "Tribalman\'s Shiv",
            "Bushwacka",
            "Shahanshah",
            ]

    @functools.cached_property
    def all_spy_watches(self) -> List[str]:
        return [
            "Invis Watch",
            "Enthusiast\'s Timepiece",
            "Quäckenbirdt",
            "Cloak and Dagger",
            "Dead Ringer",
            ]

    @functools.cached_property
    def all_spy_secondaries(self) -> List[str]:
        return [
            "Revolver",
            "Big Kill",
            "Ambassador",
            "L\'Etranger",
            "Enforcer",
            "Diamondback",
            ]

    @functools.cached_property
    def all_spy_melees(self) -> List[str]:
        return [
            "Knife",
            "Sharp Dresser",
            "Your Eternal Reward",
            "Wanga Prick",
            "Conniver\'s Kunai",
            "Big Earner",
            "Spy-cicle",
            ]

    @functools.cached_property
    def all_spy_buildings(self) -> List[str]:
        return [
            "Sapper",
            "Ap-Sap",
            "Snack Attack",
            "Red-Tape Recorder",
            ]

    @property
    def include_halloween(self) -> bool:
        return bool(self.archipelago_options.tf2_halloween.value)

    @property
    def include_smissmas(self) -> bool:
        return bool(self.archipelago_options.tf2_smissmas.value)

    @property
    def include_mvm(self) -> bool:
        return bool(self.archipelago_options.tf2_mvm.value)

    @property
    def include_alternative_gamemodes(self) -> bool:
        return bool(self.archipelago_options.tf2_alternative_gamemodes.value)

    @staticmethod
    def classes() -> List[str]:
        return [
            "Scout",
            "Soldier",
            "Pyro",
            "Demoman",
            "Engineer",
            "Medic",
            "Sniper",
            "Spy",
            ]

    @property
    def owned_scout_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_scout_primaries.value)

    @property
    def owned_scout_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_scout_secondaries.value)

    @property
    def owned_scout_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_scout_melees.value)

    @property
    def owned_soldier_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_soldier_primaries.value)

    @property
    def owned_soldier_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_soldier_secondaries.value)

    @property
    def owned_soldier_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_soldier_melees.value)

    @property
    def owned_pyro_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_pyro_primaries.value)

    @property
    def owned_pyro_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_pyro_secondaries.value)

    @property
    def owned_pyro_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_pyro_melees.value)

    @property
    def owned_demoman_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_demoman_primaries.value)

    @property
    def owned_demoman_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_demoman_secondaries.value)

    @property
    def owned_demoman_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_demoman_melees.value)

    @property
    def owned_engineer_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_engineer_primaries.value)

    @property
    def owned_engineer_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_engineer_secondaries.value)

    @property
    def owned_engineer_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_engineer_melees.value)

    @property
    def owned_heavy_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_heavy_primaries.value)

    @property
    def owned_heavy_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_heavy_secondaries.value)

    @property
    def owned_heavy_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_heavy_melees.value)

    @property
    def owned_medic_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_medic_primaries.value)

    @property
    def owned_medic_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_medic_secondaries.value)

    @property
    def owned_medic_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_medic_melees.value)

    @property
    def owned_sniper_primaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_sniper_primaries.value)

    @property
    def owned_sniper_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_sniper_secondaries.value)

    @property
    def owned_sniper_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_sniper_melees.value)

    @property
    def owned_spy_watches(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_spy_watches.value)

    @property
    def owned_spy_secondaries(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_spy_secondaries.value)

    @property
    def owned_spy_melees(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_spy_melees.value)

    @property
    def owned_spy_buildings(self) -> List[str]:
        return sorted(self.archipelago_options.tf2_owned_spy_buildings.value)

    def scout_primaries(self) -> List[str]:
        return self.owned_scout_primaries

    def scout_secondaries(self) -> List[str]:
        return self.owned_scout_secondaries

    def scout_melees(self) -> List[str]:
        return self.owned_scout_melees

    def soldier_primaries(self) -> List[str]:
        return self.owned_soldier_primaries

    def soldier_secondaries(self) -> List[str]:
        return self.owned_soldier_secondaries

    def soldier_melees(self) -> List[str]:
        return self.owned_soldier_melees

    def pyro_primaries(self) -> List[str]:
        return self.owned_pyro_primaries

    def pyro_secondaries(self) -> List[str]:
        return self.owned_pyro_secondaries

    def pyro_melees(self) -> List[str]:
        return self.owned_pyro_melees

    def demoman_primaries(self) -> List[str]:
        return self.owned_demoman_primaries

    def demoman_secondaries(self) -> List[str]:
        return self.owned_demoman_secondaries

    def demoman_melees(self) -> List[str]:
        return self.owned_demoman_melees

    def engineer_primaries(self) -> List[str]:
        return self.owned_engineer_primaries

    def engineer_secondaries(self) -> List[str]:
        return self.owned_engineer_secondaries

    def engineer_melees(self) -> List[str]:
        return self.owned_engineer_melees

    def heavy_primaries(self) -> List[str]:
        return self.owned_heavy_primaries

    def heavy_secondaries(self) -> List[str]:
        return self.owned_heavy_secondaries

    def heavy_melees(self) -> List[str]:
        return self.owned_heavy_melees

    def medic_primaries(self) -> List[str]:
        return self.owned_medic_primaries

    def medic_secondaries(self) -> List[str]:
        return self.owned_medic_secondaries

    def medic_melees(self) -> List[str]:
        return self.owned_medic_melees

    def sniper_primaries(self) -> List[str]:
        return self.owned_sniper_primaries

    def sniper_secondaries(self) -> List[str]:
        return self.owned_sniper_secondaries

    def sniper_melees(self) -> List[str]:
        return self.owned_sniper_melees

    def spy_watches(self) -> List[str]:
        return self.owned_spy_watches

    def spy_secondaries(self) -> List[str]:
        return self.owned_spy_secondaries

    def spy_melees(self) -> List[str]:
        return self.owned_spy_melees

    def spy_buildings(self) -> List[str]:
        return self.owned_spy_buildings

    def maps_ctf(self) -> List[str]:
        maps: List[str] = self.base_maps_ctf[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_ctf[:])

        if self.include_smissmas:
            maps.extend(self.smissmas_maps_ctf[:])

        return sorted(maps)

    def maps_cp(self) -> List[str]:
        maps: List[str] = self.base_maps_cp[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_cp[:])

        return sorted(maps)

    def maps_koth(self) -> List[str]:
        maps: List[str] = self.base_maps_koth[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_koth[:])

        return sorted(maps)

    def maps_ad(self) -> List[str]:
        return sorted(self.base_maps_ad[:])

    def maps_pl(self) -> List[str]:
        maps: List[str] = self.base_maps_pl[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_pl[:])

        if self.include_smissmas:
            maps.extend(self.smissmas_maps_pl[:])

        return sorted(maps)

    def maps_plr(self) -> List[str]:
        maps: List[str] = self.base_maps_plr[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_plr[:])

        return sorted(maps)

    def maps_pd(self) -> List[str]:
        maps: List[str] = self.base_maps_pd[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_pd[:])

        if self.include_smissmas:
            maps.extend(self.smissmas_maps_pd[:])

        return sorted(maps)

    def maps_vsh(self) -> List[str]:
        maps: List[str] = self.base_maps_vsh[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_vsh[:])

        if self.include_smissmas:
            maps.extend(self.smissmas_maps_vsh[:])

        return sorted(maps)

    def maps_medival(self) -> List[str]:
        maps: List[str] = self.medival_maps_ad[:]
        if self.include_halloween:
            maps.extend(self.halloween_medival_maps_ad[:])

        return sorted(maps)

    def maps_mannpower(self) -> List[str]:
        return sorted(self.base_maps_ctf_mannpower[:])

    def maps_sd(self) -> List[str]:
        maps: List[str] = self.base_maps_sd[:]
        if self.include_halloween:
            maps.extend(self.halloween_maps_sd[:])

        return sorted(maps)

    def maps_tc(self) -> List[str]:
        return sorted(self.base_maps_tc[:])

    def maps_pass(self) -> List[str]:
        return sorted(self.base_maps_pass[:])

    def maps_mvm(self) -> List[str]:
        return sorted(self.base_maps_mvm[:])

class TF2Halloween(Toggle):
    """
    Indicates whether to include Halloween content when generating objectives.
    """

    display_name = "Include Halloween Content"

class TF2Smissmas(Toggle):
    """
    Indicates whether to include Smissmas/Holiday maps when generating objectives.
    """

    display_name = "Include Halloween Content"

class TF2MVM(Toggle):
    """
    Indicates whether to include Mann Vs. Machine content when generating objectives.
    """

    display_name = "Include Mann Vs. Machine Content"

class TF2AlternativeGamemodes(Toggle):
    """
    Indicates whether to include Alternative Gamemodes when generating objectives.
    """

    display_name = "Include Alternative Gamemodes"

class TF2OwnedScoutPrimaries(OptionSet):
    """
    Indicates which Scout primaries the player owns and wants to possibly to equip.
    """

    display_name = "Scout Primaries Owned"
    valid_keys = TF2Game().all_scout_primaries

    default = valid_keys

class TF2OwnedScoutSecondaries(OptionSet):
    """
    Indicates which Scout primaries the player owns and wants to possibly to equip.
    """

    display_name = "Scout Secondaries Owned"
    valid_keys = TF2Game().all_scout_secondaries

    default = valid_keys


class TF2OwnedScoutMelees(OptionSet):
    """
    Indicates which Scout melees the player owns and wants to possibly to equip.
    """

    display_name = "Scout Melees Owned"
    valid_keys = TF2Game().all_scout_melees

    default = valid_keys

class TF2OwnedSoldierPrimaries(OptionSet):
    """
    Indicates which Soldier primaries the player owns and wants to possibly to equip.
    """

    display_name = "Soldier Primaries Owned"
    valid_keys = TF2Game().all_soldier_primaries

    default = valid_keys

class TF2OwnedSoldierSecondaries(OptionSet):
    """
    Indicates which Soldier primaries the player owns and wants to possibly to equip.
    """

    display_name = "Soldier Secondaries Owned"
    valid_keys = TF2Game().all_soldier_secondaries

    default = valid_keys


class TF2OwnedSoldierMelees(OptionSet):
    """
    Indicates which Soldier melees the player owns and wants to possibly to equip.
    """

    display_name = "Soldier Melees Owned"
    valid_keys = TF2Game().all_soldier_melees

    default = valid_keys

class TF2OwnedPyroPrimaries(OptionSet):
    """
    Indicates which Pyro primaries the player owns and wants to possibly to equip.
    """

    display_name = "Pyro Primaries Owned"
    valid_keys = TF2Game().all_pyro_primaries

    default = valid_keys

class TF2OwnedPyroSecondaries(OptionSet):
    """
    Indicates which Pyro primaries the player owns and wants to possibly to equip.
    """

    display_name = "Pyro Secondaries Owned"
    valid_keys = TF2Game().all_pyro_secondaries

    default = valid_keys


class TF2OwnedPyroMelees(OptionSet):
    """
    Indicates which Pyro melees the player owns and wants to possibly to equip.
    """

    display_name = "Pyro Melees Owned"
    valid_keys = TF2Game().all_pyro_melees

    default = valid_keys

class TF2OwnedDemomanPrimaries(OptionSet):
    """
    Indicates which Demoman primaries the player owns and wants to possibly to equip.
    """

    display_name = "Demoman Primaries Owned"
    valid_keys = TF2Game().all_demoman_primaries

    default = valid_keys

class TF2OwnedDemomanSecondaries(OptionSet):
    """
    Indicates which Demoman primaries the player owns and wants to possibly to equip.
    """

    display_name = "Demoman Secondaries Owned"
    valid_keys = TF2Game().all_demoman_secondaries

    default = valid_keys


class TF2OwnedDemomanMelees(OptionSet):
    """
    Indicates which Demoman melees the player owns and wants to possibly to equip.
    """

    display_name = "Demoman Melees Owned"
    valid_keys = TF2Game().all_demoman_melees

    default = valid_keys

class TF2OwnedEngineerPrimaries(OptionSet):
    """
    Indicates which Engineer primaries the player owns and wants to possibly to equip.
    """

    display_name = "Engineer Primaries Owned"
    valid_keys = TF2Game().all_engineer_primaries

    default = valid_keys

class TF2OwnedEngineerSecondaries(OptionSet):
    """
    Indicates which Engineer primaries the player owns and wants to possibly to equip.
    """

    display_name = "Engineer Secondaries Owned"
    valid_keys = TF2Game().all_engineer_secondaries

    default = valid_keys


class TF2OwnedEngineerMelees(OptionSet):
    """
    Indicates which Engineer melees the player owns and wants to possibly to equip.
    """

    display_name = "Engineer Melees Owned"
    valid_keys = TF2Game().all_engineer_melees

    default = valid_keys

class TF2OwnedHeavyPrimaries(OptionSet):
    """
    Indicates which Heavy primaries the player owns and wants to possibly to equip.
    """

    display_name = "Heavy Primaries Owned"
    valid_keys = TF2Game().all_heavy_primaries

    default = valid_keys

class TF2OwnedHeavySecondaries(OptionSet):
    """
    Indicates which Heavy primaries the player owns and wants to possibly to equip.
    """

    display_name = "Heavy Secondaries Owned"
    valid_keys = TF2Game().all_heavy_secondaries

    default = valid_keys


class TF2OwnedHeavyMelees(OptionSet):
    """
    Indicates which Heavy melees the player owns and wants to possibly to equip.
    """

    display_name = "Heavy Melees Owned"
    valid_keys = TF2Game().all_heavy_melees

    default = valid_keys

class TF2OwnedMedicPrimaries(OptionSet):
    """
    Indicates which Medic primaries the player owns and wants to possibly to equip.
    """

    display_name = "Medic Primaries Owned"
    valid_keys = TF2Game().all_medic_primaries

    default = valid_keys

class TF2OwnedMedicSecondaries(OptionSet):
    """
    Indicates which Medic primaries the player owns and wants to possibly to equip.
    """

    display_name = "Medic Secondaries Owned"
    valid_keys = TF2Game().all_medic_secondaries

    default = valid_keys


class TF2OwnedMedicMelees(OptionSet):
    """
    Indicates which Medic melees the player owns and wants to possibly to equip.
    """

    display_name = "Medic Melees Owned"
    valid_keys = TF2Game().all_medic_melees

    default = valid_keys

class TF2OwnedSniperPrimaries(OptionSet):
    """
    Indicates which Sniper primaries the player owns and wants to possibly to equip.
    """

    display_name = "Sniper Primaries Owned"
    valid_keys = TF2Game().all_sniper_primaries

    default = valid_keys

class TF2OwnedSniperSecondaries(OptionSet):
    """
    Indicates which Sniper primaries the player owns and wants to possibly to equip.
    """

    display_name = "Sniper Secondaries Owned"
    valid_keys = TF2Game().all_sniper_secondaries

    default = valid_keys


class TF2OwnedSniperMelees(OptionSet):
    """
    Indicates which Sniper melees the player owns and wants to possibly to equip.
    """

    display_name = "Sniper Melees Owned"
    valid_keys = TF2Game().all_sniper_melees

    default = valid_keys

class TF2OwnedSpyWatches(OptionSet):
    """
    Indicates which Spy watches the player owns and wants to possibly to equip.
    """

    display_name = "Spy Watches Owned"
    valid_keys = TF2Game().all_spy_watches

    default = valid_keys

class TF2OwnedSpySecondaries(OptionSet):
    """
    Indicates which Spy primaries the player owns and wants to possibly to equip.
    """

    display_name = "Spy Secondaries Owned"
    valid_keys = TF2Game().all_spy_secondaries

    default = valid_keys


class TF2OwnedSpyMelees(OptionSet):
    """
    Indicates which Spy melees the player owns and wants to possibly to equip.
    """

    display_name = "Spy Melees Owned"
    valid_keys = TF2Game().all_spy_melees

    default = valid_keys

class TF2OwnedSpyBuildings(OptionSet):
    """
    Indicates which Spy sappers the player owns and wants to possibly to equip.
    """

    display_name = "Spy Sappers Owned"
    valid_keys = TF2Game().all_spy_buildings

    default = valid_keys
