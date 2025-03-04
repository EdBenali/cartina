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

        self.surface = self.load_image(self.rank.col_ref, self.suit.row_ref)

        self.rect = self.surface.get_rect()

        self.update_position(pos)

    def load_image(self, col_ref, row_ref):
        surf = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/{self.suit.colour}/{col_ref * 64}_"
            f"{row_ref * 96}.png").convert_alpha()
        surf = pygame.transform.scale_by(surf, GUI_SCALE)
        return surf

    def update_position(self, pos):
         self.rect.center = pos

    def update_rotation(self, angle: int):
        """
        Rotates the sprite to the given angle.

        :param angle: int between 0 and 360
        """
        self.surface = self.load_image(self.rank.col_ref, self.suit.row_ref)
        self.surface = pygame.transform.rotate(self.surface, angle)
        self.rect = self.surface.get_rect()