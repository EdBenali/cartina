from enums import Suit, Rank, Ranks, Suits
import pygame
from pygame.locals import *

# TODO:
#   - Add card generation system
#       - Can we layer sprites on the fly, make composites? Or should we make
#       a new asset for each card combo?
#   - Add set screen regions, eg hand, play area, deck
#   - Add game logic, win states, rounds, card dealing
#       - Add bots for solo play?
#   - Clean up styling, better card sprites, better background, Balatro-esq?
#   - Add multiplayer? Online/Local
#   - Export to other languages for distribution
#

RED = pygame.Color((255, 0, 0, 255))
BLACK = pygame.Color((0, 0, 0, 255))


class App:
    def __init__(self):
        pygame.init()

        display_info = pygame.display.Info()
        self.max_w = display_info.current_w
        self.max_h = display_info.current_h
        self.screen = pygame.display.set_mode(
            [self.max_w, self.max_h],
            pygame.RESIZABLE
        )
        pygame.display.set_caption('Carto')

        self.bg = BLACK

        self.entities = []

    def main_loop(self):
        """
        Main game loop for drawing and logic.


        """
        fps = 144
        fps_clock = pygame.time.Clock()

        mouse_x, mouse_y = 0, 0
        clicked = False

        running = True

        self.entities.append(Card(Suits.Spades, Ranks.Ace))

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

            self._handle_mouse_interaction(
                mouse_x=mouse_x,
                mouse_y=mouse_y,
                clicked=clicked)

            pygame.display.update()
            fps_clock.tick(fps)

        pygame.quit()

    def _draw_scene(self):
        """
        Handles updating the screen and redrawing all scene elements.
        """
        # Draw background
        self.screen.fill(self.bg)

        # Draw Entities
        for entity in self.entities:
            self.screen.blit(entity.image, (entity.rect.x, entity.rect.y))
            pygame.draw.rect(self.screen, RED, entity.rect, 1)

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
        for entity in self.entities:
            if clicked and entity.rect.collidepoint(mouse_x, mouse_y):
                entity.rect.x = mouse_x - (entity.rect.WIDTH / 2)
                entity.rect.y = mouse_y - (entity.rect.HEIGHT / 2)


class Card(pygame.sprite.Sprite):
    """
    Basic card class this handles card game data.
    """
    def __init__(self, suit: Suit, val: Rank):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.val = val

        self.image = self.__construct_sprite()
        self.rect = pygame.Rect(
            0,
            0,
            self.image.get_width(),
            self.image.get_height())


    def __construct_sprite(self):
        return pygame.image.load("assets/ace_of_spades.png").convert()


def _float_to_int8(f: float):
    return int(round(f * 255, 1))
