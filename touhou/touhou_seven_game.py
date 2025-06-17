from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class TouhouSevenArchipelagoOptions:
    pass


class TouhouSevenGame(Game):
    name = "Touhou Youyoumu~ Perfect Cherry Blossom"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = None

    is_adult_only_or_unrated = True

    options_cls = TouhouSevenArchipelagoOptions

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
                    "SPELL_CARDS": (self.spell_cards_easy, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as CHARACTER",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_normal, 1),
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
                    "SPELL_CARDS": (self.spell_cards_hard, 1),
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
                    "SPELL_CARDS": (self.spell_cards_lunatic, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
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
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Score SCORE points or greater on SPELL_CARDS as CHARACTER",
                data={
                    "SCORE": (self.score_range, 1),
                    "SPELL_CARDS": (self.spell_cards_phantasm, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_easy, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_normal, 1),
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
                    "SPELL_CARDS": (self.spell_cards_hard, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_lunatic, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
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
                label="Graze GRAZE times or greater on SPELL_CARDS as CHARACTER",
                data={
                    "GRAZE": (self.graze_range, 1),
                    "SPELL_CARDS": (self.spell_cards_phantasm, 1),
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
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
            "Reimu Hakurei",
            "Marisa Kirisame",
            "Sakuya Izayoi",
        ]

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Cirno",
            "Letty Whiterock",
            "Chen (Stage 2 Midboss)",
            "Chen",
            "Alice Margatroid",
            "Alice Margatroid (Midboss)",
            "Prisimriver Sisters",
            "Youmu Konpaku (Stage 5 Midboss)",
            "Youmu Konpaku",
            "Youmu Konpaku (Stage 6 Midboss)",
            "Yuyuko Saigyouji",
            "Chen (Extra Stage Midboss)",
            "Ran Yakumo",
            "Ran Yakumo (Phantasm Stage Modboss)",
            "Yukari Yakumo",
        ]

    @staticmethod
    def spell_cards_easy() -> List[str]:
        return [
            "Cold Sign \"Lingering Cold -Easy-\"",
            "Winter Sign \"Flower Wither Away -Easy-\"",
            "Hermit Sign \"Fenghuang Egg -Easy-\"",
            "Shikigami Sign \"Soaring Seiman -Easy-\"",
            "Heaven Sign \"Tianxian\'s Rumbling -Easy-\"",
            "Hermit Sign \"Shikai Immortality -Easy-\"",
            "Blue Sign \"Fraternal French Dolls -Easy-\"",
            "Scarlet Sign \"Red-Haired Dutch Dolls -Easy-\"",
            "Darkness Sign \"Foggy London Dolls -Easy-\"",
            "Malediction \"Magically Luminous Shanghai Dolls -Easy-\"",
            "Noisy Sign \"Phantom Dinning -Easy-\"",
            "String Performance \"Guarneri del Gesù -Easy-\"",
            "Trumpet Spirit \"Hino Phantasm -Easy-\"",
            "Nether Keys \"Fazioli Nether Performance -Easy-\"",
            "Funeral Concert \"Prism Concerto -Easy-\"",
            "Great Funeral Concert \"Spirit Wheel Concerto Grosso -Easy-\"",
            "Ghost Sword \"Fasting of the Young Preta -Easy-\"",
            "Hell Realm Sword \"Two Hundred Yojana in One Slash -Easy-\"",
            "Animal Realm Sword \"Karmic Punishment of the Idle and Unfocused -Easy-\"",
            "Human Realm Sword \"Fantasy of Entering Enlightenment -Easy-\"",
            "Heaven Sword \"Five Signs of the Dying Deva -Easy-\"",
            "Six Realms Sword \"A Single Thought and Infinite Kalpas -Easy-\"",
            "Dead Village \"Death of One's Home -Wandering Soul-\"",
            "Deadly Dance \"Law of Mortality -Bewilderment-\"",
            "Flowery Soul \"Ghost Butterfly\"",
            "Subtle Melody \"Repository of Hirokawa -False Spirit-\"",
            "Cherry Blossom Sign \"Perfect Ink-Black Cherry Blossom -Seal-\"",
            "\"Resurrection Butterfly -10% Reflowering-\"",
        ]

    @staticmethod
    def spell_cards_normal() -> List[str]:
        return [
                "Cold Sign \"Lingering Cold\"",
                "Winter Sign \"Flower Wither Away\"",
                "Hermit Sign \"Fenghuang Egg\"",
                "Shikigami Sign \"Soaring Seiman\"",
                "Heaven Sign \"Tianxian\'s Rumbling\"",
                "Hermit Sign \"Shikai Immortality\"",
                "Blue Sign \"Fraternal French Dolls\"",
                "Scarlet Sign \"Red-Haired Dutch Dolls\"",
                "Darkness Sign \"Foggy London Dolls\"",
                "Malediction \"Magically Luminous Shanghai Dolls\"",
                "Noisy Sign \"Phantom Dinning\"",
                "String Performance \"Guarneri del Gesù\"",
                "Trumpet Spirit \"Hino Phantasm\"",
                "Nether Keys \"Fazioli Nether Performance\"",
                "Funeral Concert \"Prism Concerto\"",
                "Great Funeral Concert \"Spirit Wheel Concerto Grosso\"",
                "Ghost Sword \"Fasting of the Young Preta\"",
                "Hell Realm Sword \"Two Hundred Yojana in One Slash\"",
                "Animal Realm Sword \"Karmic Punishment of the Idle and Unfocused\"",
                "Human Realm Sword \"Fantasy of Entering Enlightenment\"",
                "Heaven Sword \"Five Signs of the Dying Deva\"",
                "Six Realms Sword \"A Single Thought and Infinite Kalpas\"",
                "Dead Village \"Death of One's Home -Past Sin-\"",
                "Deadly Dance \"Law of Mortality -Dead Butterfly-\"",
                "Flowery Soul \"Swallowtail Butterfly\"",
                "Subtle Melody \"Repository of Hirokawa -Dead Spirit-\"",
                "Cherry Blossom Sign \"Perfect Ink-Black Cherry Blossom -Self-Loss-\"",
                "\"Resurrection Butterfly -30% Reflowering-\"",
                "Subtle Melody \"Repository of Hirokawa -Deceased Spirit-\"",
            ]

    @staticmethod
    def spell_cards_hard() -> List[str]:
        return [
            "Cold Sign \"Lingering Cold -Hard-\"",
            "Frost Sign \"Frost Columns\"",
            "White Sign \"Undulation Ray\"",
            "Hermit Sign \"Fenghuang\'s Spread Wings\"",
            "Yin Yang \"Douman-Seiman\"",
            "Flight Sign \"Soaring Idaten\"",
            "Oni Sign \"Kimon Konjin\"",
            "Puppeteer Sign \"Maiden\'s Bunraku\"",
            "Blue Sign \"Fraternal French Dolls -Hard-\"",
            "White Sign \"Chalk-White Russian Dolls\"",
            "Cycle Sign \"Samsaric Tibetan Dolls\"",
            "Malediction \"Magically Luminous Shanghai Dolls -Hard-\"",
            "Noisy Sign \"Live Poltergeist\"",
            "Divine Strings \"Stradivarius\"",
            "Nether Trumpet \"Ghost Clifford\"",
            "Key Spirit \"Bösendorfer Divine Performance\"",
            "Noisy Funeral \"Stygian Riverside\"",
            "Great Funeral Concert \"Spirit Wheel Concerto Grosso: Revised\"",
            "Preta Sword \"Scroll of the Preta Realm\"",
            "Hellfire Sword \"Karmic Winds of Afterimages\"",
            "Asura Sword \"Obsession with the Present World\"",
            "Human Era Sword \"Great Enlightenment Appearing and Disappearing\"",
            "Deva Realm Sword \"Displeasure of the Seven Hakus\"",
            "Six Realms Sword \"A Single Thought and Infinite Kalpas -Hard-\"",
            "Dead Village \"Death of One's Home -Trackless Path-\"",
            "Deadly Dance \"Law of Mortality -Poisonous Moth-\"",
            "Flowery Soul \"Deep-Rooted Butterfly\"",
            "Subtle Melody \"Repository of Hirokawa -Phantom Spirit-\"",
            "Cherry Blossom Sign \"Perfect Ink-Black Cherry Blossom -Spring Sleep-\"",
        ]

    @staticmethod
    def spell_cards_lunatic() -> List[str]:
        return [
            "Frost Sign \"Frost Columns -Lunatic-\"",
            "Cold Sign \"Lingering Cold -Lunatic-\"",
            "Mystic Sign \"Table-Turning\"",
            "Hermit Sign \"Fenghuang's Spread Wings -Lunatic-\"",
            "Yin Yang \"Seiman-Daimon\"",
            "Servant Sign \"Gohou-Tendou\'s Wild Dance\"",
            "Direction Sign \"Kimontonkou\"",
            "Puppeteer Sign \"Maiden\'s Bunraku -Lunatic-\"",
            "Blue Sign \"Fraternal Orléans Dolls\"",
            "White Sign \"Chalk-White Russian Dolls -Lunatic-\"",
            "Elegant Sign \"Spring Kyoto Dolls\"",
            "Malediction \"Hanged Hourai Dolls\"",
            "Noisy Sign \"Live Poltergeist -Lunatic-\"",
            "Fake Strings \"Pseudo Stradivarius\"",
            "Nether Trumpet \"Ghost Clifford -Lunatic-\"",
            "Key Spirit \"Bösendorfer Divine Performance -Lunatic-\"",
            "Noisy Funeral \"Stygian Riverside -Lunatic-\"",
            "Great Funeral Concert \"Spirit Wheel Concerto Grosso: Wondrous\"",
            "Hungry King Sword \"Ten Kings' Retribution on the Preta\"",
            "Hell God Sword \"Karmic Winds Instant-Divine Severance\"",
            "Asura Sword \"Obsession with the Present World -Lunatic-\"",
            "Human God Sword \"Constancy of the Conventional Truth\"",
            "Heaven God Sword \"Three Kons, Seven Hakus\"",
            "Subtle Melody \"Repository of Hirokawa -Divine Spirit-\"",
            "\"Resurrection Butterfly -50% Reflowering-\"",
            "Deadly Dance \"Law of Mortality -Demon World-\"",
            "Flowery Soul \"Butterfly Delusion\"",
            "Dead Village \"Death of One's Home -Suicide-\"",
            "Cherry Blossom Sign \"Perfect Ink-Black Cherry Blossom -Bloom-\"",
            "\"Resurrection Butterfly -80% Reflowering-\"",
            "Six Realms Sword \"A Single Thought and Infinite Kalpas -Lunatic-\"",
        ]

    @staticmethod
    def spell_cards_extra() -> List[str]:
        return [
            "Oni Sign \"Blue Oni, Red Oni\"",
            "Kishin \"Soaring Bishamonten\"",
            "Shikigami \"Senko Thoughtful Meditation\"",
            "Shikigami \"Banquet of the Twelve General Gods\"",
            "Shiki Brilliance \"Kitsune-Tanuki Youkai Laser\"",
            "Shiki Brilliance \"Charming Siege from All Sides\"",
            "Shiki Brilliance \"Princess Tenko -Illusion-\"",
            "Shiki Shot \"Ultimate Buddhist\"",
            "Shiki Shot \"Unilateral Contact\"",
            "Shikigami \"Chen\"",
            "\"Kokkuri-san's Contract\"",
            "Illusion God \"Descent of Iizuna Gongen\"",
        ]

    @staticmethod
    def spell_cards_phantasm() -> List[str]:
        return [
            "Shikigami \"Protection of Zenki and Goki\"",
            "Shikigami \"Channeling Dakiniten\"",
            "Barrier \"Curse of Dreams and Reality\"",
            "Barrier \"Balance of Motion and Stillness\"",
            "Barrier \"Mesh of Light and Darkness\"",
            "Evil Spirits \"Dreamland of Straight and Curve\"",
            "Evil Spirits \"Yukari Yakumo's Spiriting Away\"",
            "Evil Spirits \"Bewitching Butterfly Living in the Zen Temple\"",
            "Sinister Spirits \"Double Black Death Butterfly\"",
            "Shikigami \"Ran Yakumo\"",
            "\"Boundary of Humans and Youkai\"",
            "Barrier \"Boundary of Life and Death\"",
            "Yukari's Arcanum \"Danmaku Barrier\"",
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
            "Phantasm",
        ]

    @staticmethod
    def graze_range() -> range:
        return range(25, 101, 5)

    @staticmethod
    def score_range() -> range:
        return range(1000, 650001, 1000)


# Archipelago Options
# ...
