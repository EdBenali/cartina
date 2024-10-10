import pygame

from components.card import Card
import unittest

from components.enums import Suits, Ranks


class TestCard(unittest.TestCase):
    def setUp(self):
        pygame.init()
        display_info = pygame.display.Info()
        screen = pygame.display.set_mode(
            [display_info.current_w, display_info.current_h],
            pygame.RESIZABLE
        )

        self.card = Card(suit=Suits.Hearts.value, rank=Ranks.King.value)

    def test_card_init(self):
        assert self.card.rank == Ranks.King.value
        assert self.card.suit == Suits.Hearts.value

    def test_card_update_position(self):
        self.card.update_position((123, 456))
        assert self.card.rect.center == (123, 456)

    def test_card_update_position_twice(self):
        self.card.update_position((123, 456))
        self.card.update_position((789, 1011))
        assert self.card.rect.center == (789, 1011)

    def test_card_update_rotation(self):
        self.card.update_rotation(90)
        assert self.card.image