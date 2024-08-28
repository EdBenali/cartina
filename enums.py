from enum import Enum
from constants import RED, BLACK


class Suit:
    def __init__(self, value: str, colour: tuple):
        self.value = value
        self.colour = colour


class RankGroup(Enum):
    Face = 'Face'
    Number = 'Number'
    Ace = 'Ace'


class Rank:
    def __init__(self, symbol: str, group: RankGroup):
        self.symbol = symbol
        self.group = group


class Suits(Enum):
    Clubs = Suit('Clubs', BLACK)
    Diamonds = Suit('Diamonds', RED)
    Hearts = Suit('Hearts', RED)
    Spades = Suit('Spades', BLACK)


class Ranks(Enum):
    Ace = Rank(symbol='A', group=RankGroup.Ace)
    Two = Rank(symbol='2', group=RankGroup.Number)
    Three = Rank(symbol='3', group=RankGroup.Number)
    Four = Rank(symbol='4', group=RankGroup.Number)
    Five = Rank(symbol='5', group=RankGroup.Number)
    Six = Rank(symbol='6', group=RankGroup.Number)
    Seven = Rank(symbol='7', group=RankGroup.Number)
    Eight = Rank(symbol='8', group=RankGroup.Number)
    Nine = Rank(symbol='9', group=RankGroup.Number)
    Ten = Rank(symbol='10', group=RankGroup.Number)
    Jack = Rank(symbol='J', group=RankGroup.Face)
    Queen = Rank(symbol='Q', group=RankGroup.Face)
    King = Rank(symbol='K', group=RankGroup.Face)
