from typing import Tuple

import pygame

from components.enums import Suit, Rank, GUI_SCALE
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

        self.image = self.load_image(self.rank.col_ref, self.suit.row_ref)

        self.rect = self.image.get_rect()

        self.update_position(pos)

    def load_image(self, col_ref, row_ref):
        img = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/{self.suit.colour}/{col_ref * 64}_"
            f"{row_ref * 96}.png").convert_alpha()
        img = pygame.transform.scale_by(img, GUI_SCALE)
        return img

    def update_position(self, pos):
         self.rect.center = pos

    def update_rotation(self, angle: int):
        """
        Rotates the sprite to the given angle.

        :param angle: int between 0 and 360
        """

        # TODO after a few rotations the image gets blurry, might have to reload
        # the image after a certain number of rotations
        self.image = self.load_image(self.rank.col_ref, self.suit.row_ref)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()