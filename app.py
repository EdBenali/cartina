from constants import BLACK, RED, TITLE

import pygame
from pygame.locals import *

from games.kings_corner.main import KingsCorner

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
global screen


class App:
    def __init__(self):
        pygame.init()
        global screen

        display_info = pygame.display.Info()
        screen = pygame.display.set_mode(
            [display_info.current_w, display_info.current_h],
            pygame.RESIZABLE
        )
        pygame.display.set_caption('Cartina')

        self.bg = BLACK

        self.game = KingsCorner(screen)

        self.deck = self.game.deck

        self.hand = self.game.hand
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
                        self.hand.add_card(card)

            self._handle_mouse_interaction(
                mouse_x=mouse_x,
                mouse_y=mouse_y)

            self.clicked, self.selected = self.game.main_loop(
                mouse_x=mouse_x,
                mouse_y=mouse_y,
                clicked=self.clicked,
                selected=self.selected)

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

        # Debugging // Draw Centre
        pygame.draw.circle(screen, RED, (screen.get_width()  // 2,
                                         screen.get_height() // 2), 10)

    def _handle_mouse_interaction(self,
                                  mouse_x: int,
                                  mouse_y: int):
        """
        Handles mouse interactions.

        :param mouse_x: int,
        :param mouse_y: int
        """
        # Deck Click
        if self.clicked and self.deck.rect.collidepoint(mouse_x, mouse_y):
            # Add card to hand
            card = self.deck.draw()
            self.entities.append(card)
            self.hand.add_card(card)
            self.clicked = False

        # Select card
        if self.clicked:
            for c in self.hand.cards:
                if c.rect.collidepoint(mouse_x, mouse_y):
                    # Realign old card
                    if self.selected:
                        self.selected.rect.y += 20

                    # Select new card
                    if c != self.selected:
                        # Bring new card to top
                        for i, entity in enumerate(self.entities):
                            if entity == c:
                                self.entities.append(self.entities.pop(i))

                        # Set new card selected
                        self.selected = c
                        # Pop up new card
                        self.selected.rect.y -= 20

                    # Drop selected card if reselected
                    else:
                        self.selected = None
                    self.clicked = False

        ## Dragging
        # for entity in self.entities:
        #     if clicked and entity.rect.collidepoint(mouse_x, mouse_y):
        #         entity.rect.x = mouse_x - (entity.rect.width / 2)
        #         entity.rect.y = mouse_y - (entity.rect.height / 2)
