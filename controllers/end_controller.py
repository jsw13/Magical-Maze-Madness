""" This module contains the EndController class """
import pygame
import pygame.locals
from views.end_view import EndView

class EndController:
    """ Controls the player input at the end of the game, after the maze. """
    def __init__(self, score, window):
        """ Initializes private views attribute. 
        
            Args:
                score (tuple): contains score, items collected, and time remaining
                window: pygame displace Surface object
        """
        self._view = EndView(score, window)

    def get_user_input(self):
        """ Gets user input and controls actions on end screen. """
        self._view.display_end()

        state = "waiting"
        while state == "waiting":
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        state = False
                    elif event.type == pygame.locals.KEYDOWN:
                        state = False
        
        return state