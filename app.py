from constants import BLACK, RED, TITLE
from enums import Suit, Rank, Ranks, Suits
import pygame
from pygame.locals import *
import random

"""
TODO:
  - Add set screen regions, eg hand, play area, deck
      - Figure out how to centre the card objects
  - Add game logic, win states, rounds, card dealing
      - Add bots for solo play?
  - Clean up styling, better card sprites, better background, Balatro-esq?
      - Shader for bg (side quest)
  - Add multiplayer? Online/Local(bots/ai)
  - Export to other languages for distribution
  - Tech debt:
      - Handle smaller resolutions/ ensure any resolution/window size works
"""

global max_w
global max_h
global screen

global clicked


class App:
    def __init__(self):
        pygame.init()

        global max_w
        global max_h
        global screen

        display_info = pygame.display.Info()
        max_w = display_info.current_w
        max_h = display_info.current_h
        screen = pygame.display.set_mode(
            [max_w, max_h],
            pygame.RESIZABLE
        )
        pygame.display.set_caption('Cartina')

        self.bg = BLACK

        self.deck = Deck()
        self.deck.add_standard_deck()
        self.deck.shuffle()

        self.hand = Hand()

        self.entities = []

    def main_loop(self):
        """
        Main game loop for drawing and logic.


        """
        global clicked

        # fps = 144
        fps_clock = pygame.time.Clock()

        mouse_x, mouse_y = 0, 0

        clicked = False

        running = True

        self.entities.append(self.deck)

        while running:
            self._draw_scene()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos

                if event.type == MOUSEBUTTONDOWN:
                    clicked = True
                elif event.type == MOUSEBUTTONUP:
                    clicked = False

                if event.type == KEYDOWN:
                    if event.key == K_d:
                        card = self.deck.draw()
                        self.entities.append(card)
                        self.hand.add_card(card)

            self._handle_mouse_interaction(
                mouse_x=mouse_x,
                mouse_y=mouse_y)

            pygame.display.update()
            fps_clock.tick()
            pygame.display.set_caption(f'{TITLE}    fps:'
                                       f'{int(fps_clock.get_fps())}')

        pygame.quit()

    def _draw_scene(self, show_collision_boundaries=True):
        """
        Handles updating the screen and redrawing all scene elements.
        """
        global screen

        # Draw background
        screen.fill(self.bg)

        # Draw Entities
        for entity in self.entities:
            screen.blit(entity.image, (entity.rect.x, entity.rect.y))

            # Debugging tool
            if show_collision_boundaries:
                pygame.draw.rect(screen, RED, entity.rect, 1)

    def _handle_mouse_interaction(self,
                                  mouse_x: int,
                                  mouse_y: int):
        """
        Handles mouse interactions.

        :param mouse_x: int,
        :param mouse_y: int
        """
        global clicked

        # Deck Click
        if clicked and self.deck.rect.collidepoint(mouse_x, mouse_y):
            # Add card to hand
            card = self.deck.draw()
            self.entities.append(card)
            self.hand.add_card(card)
            clicked = False

        ## Dragging
        # for entity in self.entities:
        #     if clicked and entity.rect.collidepoint(mouse_x, mouse_y):
        #         entity.rect.x = mouse_x - (entity.rect.width / 2)
        #         entity.rect.y = mouse_y - (entity.rect.height / 2)


class Card(pygame.sprite.Sprite):
    """
    Basic card class this handles card game data.
    """
    def __init__(self, suit: Suit, rank: Rank, pos=(100, 100)):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.rank = rank

        self.image = self.__construct_sprite()

        self.rect = pygame.Rect(
            pos[0],
            pos[1],
            self.image.get_width(),
            self.image.get_height())

    def __construct_sprite(self):
        return pygame.image.load(
            f"assets/card_gen/{self.rank.symbol}_of"
            f"_{self.suit.value}.png").convert()


class Deck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        global screen

        self.image = pygame.image.load(
            f"assets/card_gen/card_back.png").convert()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = pygame.Rect(
            screen.get_width() // 2 - self.width // 2,
            screen.get_height() // 2 - self.height // 2,
            self.width,
            self.height)

        self.__cards = []

    @property
    def length(self):
        return len(self.__cards)

    def draw(self) -> Card:
        if len(self.__cards) > 0:
            return self.__cards.pop()
        else:
            pass

    def add_standard_deck(self):
        for s in Suits:
            for r in Ranks:
                self.__cards.append(Card(suit=s.value, rank=r.value))

    def shuffle(self):
        random.shuffle(self.__cards)


class Hand:
    def __init__(self):
        global max_h
        global max_w

        self.__hand = []
        self.__pos = (max_w // 2, max_h // 1.4)
        self.__rel_positions = []

    @property
    def hand(self):
        return self.__hand

    @property
    def hand_size(self):
        return len(self.__hand)

    def add_card(self, card: Card):
        self.__hand.append(card)
        self.adjust_card_pos()

    def adjust_card_pos(self):
        self.__rel_positions.append(self.hand_size/2)
        self.__rel_positions = [p - 0.5 for p in self.__rel_positions]

        for i, c in enumerate(self.__hand):
            c.rect.center = (self.__pos[0] + self.__rel_positions[i] * c.rect.width, # ... + c.rect.width//2 for stacking cards in hand
                             self.__pos[1])


def _float_to_int8(f: float):
    return int(round(f * 255, 1))
