import logging
from copy import copy

import pygame

from components.card import Card
from components.deck import Deck
from components.enums import Ranks
from components.hand import Hand
from components.tile import Tile, CardinalPosition


class KingsCorner:
    def __init__(self, screen: pygame.surface):
        self.screen = screen


        self.deck = Deck(screen=screen,
                         pos=(screen.get_width() // 2,
                              screen.get_height() // 3))
        self.deck.add_standard_deck()
        self.deck.shuffle()

        card_size = self.deck.rect.height

        self.hand = Hand(screen)
        self.active_cards = []

        self.entities = [self.deck]

        # Initialise start tiles
        self.norm_tiles = [
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
                 card_size=card_size)]

        self.corner_tiles = [
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
        self.tiles = self.norm_tiles + self.corner_tiles
        self.entities.extend(self.tiles)

        # Initialise starting hand
        for i in range(7):
            card = self.deck.draw()
            self.active_cards.append(card)
            self.entities.append(card)
            self.hand.add_card(card)

        # Initialise normal tiles
        for tile in self.norm_tiles:
            card = self.deck.draw()
            self.entities.append(card)
            self.active_cards.append(card)
            tile.add_cards([card])

    def main_loop(self, mouse_x: int, mouse_y: int, clicked: bool,
                  selected: Card) -> (bool, Card):
        if clicked and selected:
            for tile in self.tiles:
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    clicked, selected = self.__handle_card_movement(
                        tile,
                        selected,
                        clicked)


        if self.hand.hand_size == 0:
            # TODO End game
            pass

        return clicked, selected

    def __handle_card_movement(
            self,
            tile: Tile,
            selected: Card,
            clicked: bool
    ) -> tuple:
        """


        :param tile: Tile object
        :param selected: card that is selected
        :param clicked: whether a mouse click has been registered
        :return: tuple(bool, Card)
        """
        # Get last card on tile if it is not empty
        prior = None if len(tile.cards) == 0 else tile.cards[-1]

        if tile in self.corner_tiles:
            # Valid if king to blank tile or any card on valid stack
            if self.__valid_card_stack(selected, prior=prior, corner=True):
                if selected in self.hand.cards:
                    return self.__move_card_hand_to_tile(selected, tile)
                else:
                    return self.__move_card_tile_to_tile(selected, tile)
            else:
                # TODO Communicate this to the player
                print("INVALID MOVE\nCORNER TILE")
                return clicked, selected

        elif tile in self.norm_tiles:
            # Valid for any card if tile is empty or a valid stack
            if self.__valid_card_stack(selected, prior=prior):
                if selected in self.hand.cards:
                    return self.__move_card_hand_to_tile(selected, tile)
                else:
                    return self.__move_card_tile_to_tile(selected, tile)
            else:
                # TODO Same as above
                print("INVALID MOVE:\nNORMAL TILE")
                return clicked, selected

    def __move_card_hand_to_tile(self, selected: Card, end_tile: Tile) -> (
            bool, Card):
        end_tile.add_cards([selected])
        self.hand.remove_card(selected)

        return False, None


    def __move_card_tile_to_tile(
            self,
            selected: Card,
            end_tile: Tile
    ) -> tuple:
        """
        Handle moving cards between tiles

        :param selected:
        :param end_tile:
        :return: tuple(bool, Card)
        """
        cards = None
        for tile in self.tiles:
            if selected in tile.cards:
                cards = tile.remove_card(selected)
                break
        # TODO need to fix the card draw position when moving a stack of cards
        end_tile.add_cards(cards)
        return False, None

    @staticmethod
    def __valid_card_stack(selected: Card, prior: Card, corner: bool = False) -> bool:
        """
        Ensures only valid card movements are permitted.

        :param selected: Card object; the selected card to add to the stack.
        :param prior: Card object; the last card on the stack to place the
        selected card on.
        :param corner: bool; whether the tile is a corner tile.
        :return: bool
        """
        if prior is None:
            if not corner:
                return True
            elif selected.rank == Ranks.King.value:
                return True
            else:
                return False

        # Prior card must be one rank higher and the opposite colour to be
        # valid
        if (selected.suit.colour != prior.suit.colour) and (
            selected.rank.col_ref == prior.rank.col_ref - 1):
            return True

        return False
