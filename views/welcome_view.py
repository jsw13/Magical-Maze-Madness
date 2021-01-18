""" This module contains the WelcomeView Class. """
import pygame
import pygame.locals

class WelcomeView:
    """ Displays the welcome view before the game starts. """
    def __init__(self, window):
        self._window = window

    def display_welcome(self):
        """ Displays welcome text in window. """
        # Background color
        self._window.fill((0, 0, 0))

        # Font
        pygame.font.init()
        couriernew = pygame.font.SysFont('couriernew', 24)

        # Text content
        text = self._create_display_text()
        for index in range(len(text)):
            # Text color = (255, 255, 255)
            text_surface = couriernew.render(text[index], True, (255, 255, 255))
            text_x = (self._window.get_width() - text_surface.get_width()) / 2
            text_y = (self._window.get_height() / len(text)) * index + (((self._window.get_height() / len(text)) - text_surface.get_height()) / 2)
            self._window.blit(text_surface, (text_x, text_y))

        pygame.display.update()

    def _create_display_text(self):
        """ Gets welcome text as list of strings. """
        line = "=" * int(self._window.get_width()/14)
        text = [
            line,
            "Welcome to the Maze Game!",
            line,
            "Collect items to unlock",
            "the door. Get as many as",
            "you can and reach the exit",
            "before time runs out ...",
            line,
            "w = up   ",
            "a = left ",
            "s = down ",
            "d = right",
            line,
            "Press s to start",
            "Press q to quit",
            line
        ]

        return text