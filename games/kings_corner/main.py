import pygame

from components.card import Card
from components.deck import Deck
from components.hand import Hand
from components.tile import Tile, CardinalPosition


class KingsCorner:
    def __init__(self, screen):
        self.screen = screen

        self.deck = Deck(screen=screen,
                         pos=(screen.get_width() // 2,
                              screen.get_height() // 3))
        self.deck.add_standard_deck()
        self.deck.shuffle()

        card_size = self.deck.rect.height

        self.hand = Hand(screen)

        self.entities = [self.deck]

        # Initialise start tiles
        self.tiles = [
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.NORTH,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.EAST,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.SOUTH,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.WEST,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.NORTH_EAST,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.SOUTH_EAST,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.SOUTH_WEST,
                 card_size=card_size),
            Tile(pos=self.deck.rect.center,
                 cardinal=CardinalPosition.NORTH_WEST,
                 card_size=card_size),
        ]

        self.entities.extend(self.tiles)

        # Initialise starting hand
        for i in range(7):
            card = self.deck.draw()
            self.entities.append(card)
            self.hand.add_card(card)

    def main_loop(self, mouse_x: int, mouse_y: int, clicked: bool,
                  selected: Card) -> (bool, Card):
        # Check for tile interaction
        if clicked and selected:
            for tile in self.tiles:
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    tile.cards.append(selected)
                    self.hand.remove_card(selected)

                    selected.update_rotation(tile.angle)

                    number_of_cards = len(tile.cards) - 1
                    pos = tile.rect.center
                    selected.update_position(
                        (
                            pos[0] + (tile.position[0] * tile.card_size // 3 *
                                  number_of_cards),
                            pos[1] + (tile.position[1] * tile.card_size // 3 *
                                  number_of_cards)
                        )
                    )


                    selected = None
                    clicked = False

        return clicked, selected