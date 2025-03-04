from constants import BLACK, RED, TITLE, WHITE

import pygame
from pygame.locals import *

from games.kings_corner.main import KingsCorner

"""
TODO:
  - Add game logic, win states, rounds, card dealing
      - Add bots for solo play?
  - Clean up styling, better card sprites, better background, Balatro-esq?
      - Shader for bg (side quest)
  - Add multiplayer? Online/Local(bots/ai)
  - Export to other languages for distribution
  - Tech debt:
      - Handle smaller resolutions/ ensure any resolution/window size works
"""
global screen


class App:
    def __init__(self):
        pygame.init()
        global screen

        # display_info = pygame.display.Info()
        screen = pygame.display.set_mode(
            [1920, 1080])
        pygame.display.set_caption('Cartina')

        self.bg = BLACK

        self.game = KingsCorner(screen)

        self.deck = self.game.deck

        self.hand = self.game.hand
        self.active_cards = self.game.active_cards
        self.entities = self.game.entities


        self.clicked = False
        self.selected = None

    def main_loop(self):
        """
        Main game loop for drawing and logic.


        """
        fps_clock = pygame.time.Clock(# fps = 144
            )

        mouse_x, mouse_y = 0, 0

        running = True

        while running:
            self._draw_scene()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos

                if event.type == MOUSEBUTTONDOWN:
                    self.clicked = True
                elif event.type == MOUSEBUTTONUP:
                    self.clicked = False

                if event.type == KEYDOWN:
                    if event.key == K_d:
                        card = self.deck.draw()
                        self.entities.append(card)
                        self.active_cards.append(card)
                        self.hand.add_card(card)

            self.clicked, self.selected = self.game.main_loop(
                mouse_x=mouse_x,
                mouse_y=mouse_y,
                clicked=self.clicked,
                selected=self.selected)

            self._mouse_interaction(
                mouse_x=mouse_x,
                mouse_y=mouse_y)

            pygame.display.update()
            fps_clock.tick()
            pygame.display.set_caption(f'{TITLE}    fps:'
                                       f'{int(fps_clock.get_fps())}')

        pygame.quit()

    def _draw_scene(self, debugging=False):
        """
        Handles updating the screen and redrawing all scene elements.
        """
        global screen

        # Draw background
        # TODO: add background shader CRT-1 + others
        screen.fill(self.bg)


        # Draw Entities
        for entity in self.entities:
            # TODO: need to add z-index to prevent bad overlap CRT-2
            screen.blit(entity.surface, (entity.rect.x, entity.rect.y))

            # Debugging tool
            if debugging:
                pygame.draw.rect(screen, RED, entity.rect, 1)

        if  debugging:
            # Debugging // Draw Centre
            pygame.draw.circle(screen, RED, (screen.get_width()  // 2,
                                         screen.get_height() // 2), 10)

    def _mouse_interaction(self,
                                  mouse_x: int,
                                  mouse_y: int):
        """
        Handles mouse interactions.

        :param mouse_x: int,
        :param mouse_y: int
        """
        self._deck_click(mouse_x, mouse_y)

        self._card_click(mouse_x, mouse_y)

        # # Dragging
        # for entity in self.entities:
        #     if self.clicked and entity.rect.collidepoint(mouse_x, mouse_y):
        #         entity.rect.center = (mouse_x, mouse_y)

    def _card_click(self, mouse_x, mouse_y):
        # Select card
        if self.clicked:
            for c in self.active_cards:
                if c.rect.collidepoint(mouse_x, mouse_y):
                    # Select new card
                    if not self.selected:
                        # TODO Figure out how to do highlighting

                        # Set new card selected
                        self.selected = c

                        # Pop up new card
                        pos = self.selected.rect.center
                        self.selected.update_position((pos[0], pos[1] - 20))
                    # Deselect card
                    elif c == self.selected:
                        pos = self.selected.rect.center
                        self.selected.update_position((pos[0], pos[1] + 20))
                        self.selected = None
                    self.clicked = False

    def _deck_click(self, mouse_x, mouse_y):
        # Deck Click
        if self.clicked and self.deck.rect.collidepoint(mouse_x, mouse_y):
            # Add card to hand
            card = self.deck.draw()
            self.entities.append(card)
            self.hand.add_card(card)
            self.active_cards.append(card)
            self.clicked = False
