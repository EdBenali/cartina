from enum import Enum
from constants import RED, BLACK


class Suit:
    def __init__(self, value: str, colour: tuple):
        self.value = value
        self.colour = colour


class Rank:
    def __init__(self, symbol: str):
        self.symbol = symbol

class Suits(Enum):
    Clubs = Suit('Clubs', BLACK)
    Diamonds = Suit('Diamonds', RED)
    Hearts = Suit('Hearts', RED)
    Spades = Suit('Spades', BLACK)


class Ranks(Enum):
    Ace = Rank('A')
    Two = Rank('2')
    Three = Rank('3')
    Four = Rank('4')
    Five = Rank('5')
    Six = Rank('6')
    Seven = Rank('7')
    Eight = Rank('8')
    Nine = Rank('9')
    Ten = Rank('10')
    Jack = Rank('J')
    Queen = Rank('Q')
    King = Rank('K')

