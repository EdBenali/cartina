from enum import Enum
from typing import List

import pygame

from components.card import Card
from components.enums import GUI_SCALE
from constants import CARD_SPRITE_DIR

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, cardinal, card_size):
        pygame.sprite.Sprite.__init__(self)
        self.angle = cardinal.value['angle']
        self.offset = cardinal.value['offset']
        self.card_size = card_size

        self.image = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/black_white/0_384.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, GUI_SCALE)

        self.image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.center = (pos[0] + self.offset[0] * card_size * 1.5,
                            pos[1] + self.offset[1] * card_size * 1.5)

        self.cards = []

    @property
    def length(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)
        number_of_cards = self.length - 1
        pos = self.rect.center

        for card in cards:
            card.update_rotation(self.angle)

            card.update_position(
                (
                    pos[0] + (self.offset[0] * self.card_size // 3 *
                              number_of_cards),
                    pos[1] + (self.offset[1] * self.card_size // 3 *
                              number_of_cards)
                )
            )

    def remove_card(self, selected: Card) -> List[Card]:
        cards = []
        for i, card in enumerate(self.cards):
            if card == selected:
                card.update_rotation(angle=0)

                cards = self.cards[i:]
                self.cards = self.cards[:i]
                break
        return cards


class CardinalPosition(Enum):
    NORTH = {'angle' : 0,
             'offset': (0, 1)}
    EAST = {'angle' : 90,
            'offset': (1, 0)}
    SOUTH = {'angle' : 180,
             'offset': (0, -1)}
    WEST = {'angle' : 270,
            'offset': (-1, 0)}
    NORTH_EAST = {'angle' : 45,
                  'offset': (1, 1)}
    SOUTH_EAST = {'angle' : 135,
                  'offset': (1, -1)}
    SOUTH_WEST = {'angle' : 225,
                  'offset': (-1, -1)}
    NORTH_WEST = {'angle' : 315,
                  'offset': (-1, 1)}