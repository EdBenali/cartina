from enum import Enum

import pygame

from constants import CARD_SPRITE_DIR

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, cardinal, card_size):
        pygame.sprite.Sprite.__init__(self)
        self.angle = cardinal.value['angle']
        self.position = cardinal.value['position']
        self.card_size = card_size

        self.image = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/black_white/0_384.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)

        self.image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.center = (pos[0] + self.position[0] * card_size * 1.5,
                            pos[1] + self.position[1] * card_size * 1.5)

        self.cards = []


class CardinalPosition(Enum):
    NORTH = {'angle' : 0,
             'position': (0, 1)}
    EAST = {'angle' : 90,
            'position': (1, 0)}
    SOUTH = {'angle' : 180,
             'position': (0, -1)}
    WEST = {'angle' : 270,
            'position': (-1, 0)}
    NORTH_EAST = {'angle' : 45,
                  'position': (1, 1)}
    SOUTH_EAST = {'angle' : 135,
                  'position': (1, -1)}
    SOUTH_WEST = {'angle' : 225,
                  'position': (-1, -1)}
    NORTH_WEST = {'angle' : 315,
                  'position': (-1, 1)}