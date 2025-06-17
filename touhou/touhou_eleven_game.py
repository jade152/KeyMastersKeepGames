from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class TouhouElevenArchipelagoOptions:
    pass


class TouhouElevenGame(Game):
    name = "Touhou Chireiden ~ Subterranean Animism"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = None

    is_adult_only_or_unrated = True

    options_cls = TouhouElevenArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete a trial without losing a life",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Complete a trial without losing a life and without using a bomb",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as CHARACTER",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_easy_normal, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as CHARACTER",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_hard_lunatic, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as CHARACTER",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_extra, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Reimu A on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_a, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Reimu B on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_b, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Reimu C on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_c, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Marisa A on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_a, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Marisa B on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_b, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as Marisa C on DIFFICULTY",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_c, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_easy_normal, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_hard_lunatic, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_extra, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Reimu A on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_a, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Reimu B on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_b, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Reimu C on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_reimu_c, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Marisa A on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_a, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Marisa B on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_b, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score GRAZE times or greater on SPELL_CARDS as Marisa C on DIFFICULTY",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_marisa_c, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat BOSS as CHARACTER on Easy",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat BOSS as CHARACTER on Normal",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat BOSS as CHARACTER on Hard",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat BOSS as CHARACTER on Lunatic",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat STAGE as CHARACTER on Easy",
                data={
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat STAGE as CHARACTER on Normal",
                data={
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat STAGE as CHARACTER on Hard",
                data={
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat STAGE as CHARACTER on Lunatic",
                data={
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game on Easy as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game on Normal as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game on Hard as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game on Lunatic as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game with using a continue on Easy as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game without using a continue on Normal as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game without using a continue on Hard as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat the game without using a continue on Lunatic as CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def player_characters() -> List[str]:
        return [
            "Reimu A",
            "Reimu B",
            "Reimu C",
            "Marisa A",
            "Marisa B",
            "Marisa C",
        ]

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Kisume",
            "Yamame Kurodani",
            "Parsee Mizuhashi (Stage 2 Midboss)",
            "Parsee Mizuhashi",
            "Yuugi Hoshiguma",
            "Yuugi Hoshiguma (Midboss)",
            "Satori Komeiji",
            "Rin Kaenbyou (Stage 5 Midboss)",
            "Rin Kaenbyou",
            "Rin Kaenbyou (Stage 6 Midboss)",
            "Rin Kaenbyou",
            "Sanae Kochiya (Extra Stage Midboss)",
            "Koishi Komeiji",
        ]


    @staticmethod
    def spell_cards_easy_normal() -> List[str]:
        return [
            "Recollection \"Terrible Souvenir\"",
            "Trap Sign \"Capture Web\"",
            "Miasma Sign \"Filled Miasma\"",
            "Jealousy Sign \"Green-Eyed Monster\"",
            "Grandpa Hanasaka \"Jealousy of the Kind and Lovely\"",
            "Tongue-Cut Sparrow \"Hate for the Humble and Rich\"",
            "Malice Sign \"Shrine Visit in the Dead of Night\"",
            "Mysterious Ring \"Hell\'s Wheel of Pain\"",
            "Feat of Strength \"Storm on Mt. Ooe\"",
            "Cat Sign \"Cat\'s Walk\"",
            "Cursed Sprite \"Zombie Fairy\"",
            "Malicious Spirit \"Spleen Eater\"",
            "Atonement \"Former Hell\'s Needle Mountain\"",
            "\"Rekindling of Dead Ashes\"",
            "Atomic Fire \"Nuclear Fusion\"",
            "Explosion Sign \"Petit Flare\"",
            "Explosion Sign \"Mega Flare\"",
            "Blazing Star \"Fixed Star\"",
            "\"Hell and Heaven Meltdown\"",
        ]

    @staticmethod
    def spell_cards_hard_lunatic() -> List[str]:
        return [
            "Recollection \"Terrifying Hypnotism\"",
            "Horror \"Tsurube-Otoshi Apparition\"",
            "Spider \"Cave Spider\'s Nest\"",
            "Miasma \"Unexplained Fever\"",
            "Envy \"Green-Eyed Invisible Monster\"",
            "Grandpa Hanasaka \"Shiro\'s Ashes\"",
            "Tongue-Cut Sparrow \"Large Box and Small Box\"",
            "Malice Sign \"Day 7 of the Shrine Visits in the Dead of Night\"",
            "Shackles Sign \"Shackles a Criminal Can\'t Take Off\"",
            "Feat of Strength \"Wind Blowing Down from Mt. Ooe\"",
            "Cat Sign \"Vengeful Cat Spirit's Erratic Step\"",
            "Cursed Sprite \"Fairies Possessed by Vengeful Spirits\"",
            "Corpse Spirit \"Vengeful Cannibal Spirit\"",
            "Atonement \"The Needles of Yore and the Vengeful Spirits in Pain\"",
            "\"Small Demon\'s Revival\"",
            "Atomic Fire \"Nuclear Excursion\"",
            "Explosion Sign \"Giga Flare\"",
            "Explosion Sign \"Peta Flare\"",
            "Blazing Star \"Planetary Revolution\"",
            "\"Hell\'s Tokamak\"",
        ]

    @staticmethod
    def spell_cards_extra() -> List[str]:
        return [
            "Esoterica \"Nine Syllable Stabs\"",
            "Miracle \"Miracle Fruit\"",
            "Divine Virtue \"Bumper Crop Rice Shower\"",
            "Representation \"All Ancestors Standing Beside Your Bed\"",
            "Representation \"Danmaku Paranoia\"",
            "Instinct \"Release of the Id\"",
            "Suppression \"Super-Ego\"",
            "Response \"Youkai Polygraph\""
            "Unconscious \"Rorschach in Danmaku\"",
            "Rekindled \"The Embers of Love\"",
            "Depths \"Genetics of the Unconscious\""
            "\"Philosophy of the Despised\"",
            "\"Subterranean Rose\""
        ]

    @staticmethod
    def spell_cards_reimu_a() -> List[str]:
        return [
            "Recollection \"Double Black Death Butterfly\"",
            "Recollection \"Flying Insects\' Nest\"",
            "Recollection \"Boundary of Wave and Particle\"",
            ]

    @staticmethod
    def spell_cards_reimu_b() -> List[str]:
        return [
            "Recollection \"Mt. Togakushi Toss\"",
            "Recollection \"Night Parade of a Million Demons\"",
            "Recollection \"Deep Fog Labyrinth\"",
            ]

    @staticmethod
    def spell_cards_reimu_c() -> List[str]:
        return [
            "Recollection \"Wind God\'s Leaf-Veiling\"",
            "Recollection \"Tengu\'s Macroburst\"",
            "Recollection \"Torii Whorl-Wind\"",
            ]

    @staticmethod
    def spell_cards_marisa_a() -> List[str]:
        return [
            "Recollection \"Spring Kyoto Dolls\"",
            "Recollection \"Straw Doll Kamikaze\"",
            "Recollection \"Return Inanimateness\""
            ]

    @staticmethod
    def spell_cards_marisa_b() -> List[str]:
        return [
            "Recollection \"Princess Undine\"",
            "Recollection \"Mercury Poison\"",
            "Recollection \"Philosopher\'s Stone\""
            ]

    @staticmethod
    def spell_cards_marisa_c() -> List[str]:
        return [
            "Recollection \"Exteeeending Aaaaarm\"",
            "Recollection \"Kappa\'s Pororoca\"",
            "Recollection \"Trauma in the Glimmering Depths\""
            ]

    @staticmethod
    def spell_cards_all() -> List[str]:
        return [ 
            "Oni Sign \"Anomalies, Strength, Disorder, and Spirits\"",
            "Big Four Arcanum \"Knock Out In Three Steps\"",
            "Youkai \"Blazing Wheel\"",
            ]

    @staticmethod
    def difficulties() -> List[str]:
        return [
            "Easy",
            "Normal",
            "Hard",
            "Lunatic"
            ]

    @staticmethod
    def stages() -> List[str]:
        return [
            "1",
            "2",
            "3",
            "4",
            "5",
            "Extra",
        ]

    @staticmethod
    def graze_range() -> range:
        return range(25, 101, 5)

    @staticmethod
    def score_range() -> range:
        return range(1000, 650001, 1000)


# Archipelago Options
# ...
