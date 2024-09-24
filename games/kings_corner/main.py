from components.card import Card
from components.deck import Deck
from components.enums import Ranks
from components.hand import Hand
from components.tile import Tile, CardinalPosition

REDS = ('Diamonds', 'Hearts')
BLACKS = ('Spades', 'Clubs')
RANK_ORDER = (Ranks.King.value, Ranks.Queen.value, Ranks.Jack.value,
              Ranks.Ten.value, Ranks.Nine.value, Ranks.Eight.value,
              Ranks.Seven.value, Ranks.Six.value, Ranks.Five.value,
              Ranks.Four.value, Ranks.Three.value, Ranks.Two.value,
              Ranks.Ace.value)


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
            self.entities.append(card)
            self.hand.add_card(card)

        # Initialise normal tiles
        for tile in self.norm_tiles:
            card = self.deck.draw()
            self.entities.append(card)
            tile.add_card(card)

    def main_loop(self, mouse_x: int, mouse_y: int, clicked: bool,
                  selected: Card) -> (bool, Card):
        # Check card from hand to tile interaction
        if clicked and selected:
            for tile in self.tiles:
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    clicked, selected = self.__handle_tiles(
                        tile,
                        selected,
                        clicked)
        # TODO add card from tile to til interaction

        # TODO add end on hand empty
        return clicked, selected

    def __handle_tiles(self, tile: Tile, selected: Card, clicked: bool):
        if tile in self.corner_tiles:
            if ((selected.rank == Ranks.King.value and tile.length == 0) or
                tile.length> 0 and self.__valid_card_stack(selected,
                                                    prior=tile.cards[-1])):
                return self.__add_card_to_tile(selected, tile)
            else:
                print("Invalid move")
                return clicked, selected

        elif tile in self.norm_tiles:
            if ((tile.length == 0) or
                self.__valid_card_stack(selected, prior=tile.cards[-1])):
                return self.__add_card_to_tile(selected, tile)
            else:
                print("Invalid move")
                return clicked, selected

    def __add_card_to_tile(self, selected, tile):
        tile.add_card(selected)
        self.hand.remove_card(selected)


        return False, None

    @staticmethod
    def __valid_card_stack(selected: Card, prior: Card) -> bool:
        if (selected.suit.colour != prior.suit.colour) and (
            selected.rank == RANK_ORDER[RANK_ORDER.index(prior.rank) + 1]):
            return True

        return False
