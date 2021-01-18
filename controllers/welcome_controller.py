""" This module contains the WelcomeController class """
import pygame
import pygame.locals
from views.welcome_view import WelcomeView

class WelcomeController:
    """ Controls the player input at the start of the game, before the maze. """
    def __init__(self, maze, window):
        """ Initializes private attribute. 
        
            Args:
                maze (Maze): maze object
                window: pygame display Surface object
        """
        self._maze = maze
        self._views = WelcomeView(window)

    def set_up_game(self):
        """ Adds items to random locations on the maze. """
        self._maze.add_items()

    def get_user_input(self):
        """ Gets user input and controls actions on welcome screen. """

        state = "waiting"
        while state == "waiting":

            self._views.display_welcome()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    state = "quit"

                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_s:
                        self.set_up_game()
                        state = "start"

                    if event.key in [pygame.locals.K_q, pygame.locals.K_ESCAPE]:
                        state = "quit"
    
        return state
        
