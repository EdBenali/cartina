from enum import Enum

from constants import BLACK_CARD_THEME, RED_CARD_THEME


class Suit:

    def __init__(self, suit: str, colour: tuple):
        self.suit = suit
        self.colour = colour
        self.__calc_row_ref()

    def __calc_row_ref(self):
        if self.suit == 'Clubs':
            self.row_ref = 0
        elif self.suit == 'Hearts':
            self.row_ref = 1
        elif self.suit == 'Spades':
            self.row_ref = 2
        elif self.suit == 'Diamonds':
            self.row_ref = 3


class RankGroup(Enum):
    Face = 'Face'
    Number = 'Number'
    Ace = 'Ace'


class Rank:
    def __init__(self, rank: str, group: RankGroup):
        self.rank = rank
        self.group = group
        self.__calc_col_ref()

    def __calc_col_ref(self):
        if self.group == RankGroup.Number:
            self.col_ref = int(self.rank) - 1
        elif self.rank == 'A':
            self.col_ref = 0
        elif self.rank == 'J':
            self.col_ref = 10
        elif self.rank == 'Q':
            self.col_ref = 11
        elif self.rank == 'K':
            self.col_ref = 12



class Suits(Enum):
    Clubs = Suit(suit='Clubs', colour=BLACK_CARD_THEME)
    Diamonds = Suit(suit='Diamonds', colour=RED_CARD_THEME)
    Hearts = Suit(suit='Hearts', colour=RED_CARD_THEME)
    Spades = Suit(suit='Spades', colour=BLACK_CARD_THEME)


class Ranks(Enum):
    Ace = Rank(rank='A', group=RankGroup.Ace)
    Two = Rank(rank='2', group=RankGroup.Number)
    Three = Rank(rank='3', group=RankGroup.Number)
    Four = Rank(rank='4', group=RankGroup.Number)
    Five = Rank(rank='5', group=RankGroup.Number)
    Six = Rank(rank='6', group=RankGroup.Number)
    Seven = Rank(rank='7', group=RankGroup.Number)
    Eight = Rank(rank='8', group=RankGroup.Number)
    Nine = Rank(rank='9', group=RankGroup.Number)
    Ten = Rank(rank='10', group=RankGroup.Number)
    Jack = Rank(rank='J', group=RankGroup.Face)
    Queen = Rank(rank='Q', group=RankGroup.Face)
    King = Rank(rank='K', group=RankGroup.Face)
