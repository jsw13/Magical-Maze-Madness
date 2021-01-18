""" This module contains the GameController class """
import pygame
import pygame.locals
from views.game_view import GameView

class GameController:
    """ Controller to handle the movement of the player. """
    def __init__(self, maze, window, time):
        """ Initializes private attributes.

        Args:
            maze (Maze): maze object
            windoe: pygame display Surface object
        """
        self._maze = maze
        self._view = GameView(self._maze.maze, window)
        self._time = time

    def get_user_input(self):
        """ Controller logic. Loops to get user input while game is not over. """
        # Clock object to keep track of time
        clock = pygame.time.Clock()
        # Countdown timer
        timer = self._time
        dt = 0

        direction = "down"

        self._view.display_maze(self._time, direction)
        
        pygame.key.set_repeat(150, 75)

        state = "running"
        while state == "running":
            # Decrease timer
            timer -= dt
            dt = clock.tick(30)/1000

            self._maze.open_exit()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    state = False
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key in [pygame.locals.K_q, pygame.locals.K_ESCAPE]:
                        state = False
                    if event.key in [pygame.locals.K_w, pygame.locals.K_UP]:
                        direction = "up"
                        self._maze.move_player(-1, 0)
                    if event.key in [pygame.locals.K_a, pygame.locals.K_LEFT]:
                        direction ="left"
                        self._maze.move_player(0, -1)
                    if event.key in [pygame.locals.K_s, pygame.locals.K_DOWN]:
                        self._maze.move_player(1, 0)
                        direction = "down"
                    if event.key in [pygame.locals.K_d, pygame.locals.K_RIGHT]:
                        direction = "right"
                        self._maze.move_player(0, 1)

            self._view.display_maze(timer, direction)

            if self._maze.is_exit() or timer <= 0:
                state = "finished"
                self._time = timer
                if self._time <= 0:
                    self._time = 0
        
        return state

    def check_score(self):
        """ Get the score of the player. """
        # If player reaches the exit before time expires
        final_score = int((5 - self._maze.items_remaining())*(self._time)*(100))
        score = (final_score, 5 - self._maze.items_remaining(), self._time)

        return score
            