from typing import Tuple

import pygame

from components.enums import Suit, Rank
from constants import CARD_SPRITE_DIR


class Card(pygame.sprite.Sprite):
    """
    Basic card class this handles card game data.
    """
    def __init__(self, suit: Suit, rank: Rank, pos:Tuple=(0, 0)):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.rank = rank

        self.rect = None
        self.image = None
        self.__init_sprite()
        self.update_position(pos)



    def __init_sprite(self):
        col = self.rank.col_ref
        row = self.suit.row_ref

        img = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/{self.suit.colour}/{col*64}_"
            f"{row*96}.png").convert_alpha()
        img = pygame.transform.scale_by(img, 2)

        self.image = img
        self.rect = self.image.get_rect()

    def update_position(self, pos):
         self.rect.center = pos

    def update_rotation(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()