from constants import BLACK, RED, TITLE
from enums import Suit, Rank, Ranks, Suits
import pygame
from pygame.locals import *
import random

# TODO:
#   - Add set screen regions, eg hand, play area, deck
#   - Add game logic, win states, rounds, card dealing
#       - Add bots for solo play?
#   - Clean up styling, better card sprites, better background, Balatro-esq?
#   - Add multiplayer? Online/Local
#   - Export to other languages for distribution
#   - Tech debt:
#       - Handle smaller resolutions

global max_w
global max_h
global screen


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

        self.hand = []

        self.entities = [self.deck]

    def main_loop(self):
        """
        Main game loop for drawing and logic.


        """
        # fps = 144
        fps_clock = pygame.time.Clock()

        mouse_x, mouse_y = 0, 0
        clicked = False

        running = True

        # self.entities.append(Card(Suits.Spades.value, Ranks.Ace.value))

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
                    if event.key == K_w:
                        self.entities.append(self.deck.draw())

            self._handle_mouse_interaction(
                mouse_x=mouse_x,
                mouse_y=mouse_y,
                clicked=clicked)

            pygame.display.update()
            fps_clock.tick()
            pygame.display.set_caption(f'{TITLE}    fps:'
                                       f'{int(fps_clock.get_fps())}')

        pygame.quit()

    def _draw_scene(self, show_collision_boundaries=False):
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
                                  mouse_y: int,
                                  clicked: bool):
        """
        Handles mouse interactions.

        :param mouse_x: int,
        :param mouse_y: int,
        :param clicked: bool
        """
        ## Dragging
        # for entity in self.entities:
        #     if clicked and entity.rect.collidepoint(mouse_x, mouse_y):
        #         entity.rect.x = mouse_x - (entity.rect.width / 2)
        #         entity.rect.y = mouse_y - (entity.rect.height / 2)


class Card(pygame.sprite.Sprite):
    """
    Basic card class this handles card game data.
    """
    def __init__(self, suit: Suit, rank: Rank):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.rank = rank

        self.image = self.__construct_sprite()
        self.rect = pygame.Rect(
            0,
            0,
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

        self.rect = pygame.Rect(
            screen.get_width() // 2,
            screen.get_height() // 2,
            self.image.get_width(),
            self.image.get_height())

        self.__cards = []

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


def _float_to_int8(f: float):
    return int(round(f * 255, 1))
