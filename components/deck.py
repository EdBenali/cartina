import random

import pygame

from components.card import Card
from components.enums import Suits, Ranks, GUI_SCALE
from constants import CARD_SPRITE_DIR


class Deck(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        pygame.sprite.Sprite.__init__(self)

        surface = pygame.image.load(
            f"assets/{CARD_SPRITE_DIR}/black_white/192_384.png"
            ).convert_alpha()

        self.surface = pygame.transform.scale_by(surface, GUI_SCALE)

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.rect = pygame.Rect(
            0,
            0,
            self.width,
            self.height)

        self.rect.center = pos

        self.__cards = []
        self.empty = True

    @property
    def length(self):
        return len(self.__cards)

    def draw(self) -> Card:
        if len(self.__cards) == 0:
            self.empty = True
        if not self.empty:
            return self.__cards.pop()

    def add_standard_deck(self):
        for s in Suits:
            for r in Ranks:
                self.__cards.append(Card(suit=s.value, rank=r.value))
        self.empty = False

    def shuffle(self):
        if not self.empty:
            random.shuffle(self.__cards)