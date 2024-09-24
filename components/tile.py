from enum import Enum

import pygame

from constants import CARD_SPRITE_DIR

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, cardinal, card_size):
        pygame.sprite.Sprite.__init__(self)
        self.angle = cardinal.value['angle']
        self.image = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/black_white/0_384.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)

        self.image = pygame.transform.rotate(self.image, cardinal.value['angle'])

        self.rect = self.image.get_rect()
        self.rect.center = (pos[0] + cardinal.value['offset'][0] * card_size,
                            pos[1] + cardinal.value['offset'][1] * card_size)

        self.cards = []


class CardinalPosition(Enum):
    NORTH = {'angle' : 0,
             'offset': (0, 1.5)}
    EAST = {'angle' : 90,
            'offset': (1.5, 0)}
    SOUTH = {'angle' : 180,
             'offset': (0, -1.5)}
    WEST = {'angle' : 270,
            'offset': (-1.5, 0)}
    NORTH_EAST = {'angle' : 45,
                  'offset': (1.5, 1.5)}
    SOUTH_EAST = {'angle' : 135,
                  'offset': (1.5, -1.5)}
    SOUTH_WEST = {'angle' : 225,
                  'offset': (-1.5, -1.5)}
    NORTH_WEST = {'angle' : 315,
                  'offset': (-1.5, 1.5)}