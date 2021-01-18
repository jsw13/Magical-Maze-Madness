""" This module contains the EndView class. """
import pygame
import pygame.locals

class EndView:
    """ Displays the end view after the game is over. """
    def __init__(self, score, window):
        """ Initializes the private attribute result. 
        
        Args:
            result (bool): True if wins game, False if loses game
        """
        self._score = score
        self._window = window

    def display_end(self):
        """ Prints the end screen text to the display. """
        # Background color = (0, 0, 0) = black
        self._window.fill((0, 0, 0))

        # Font = courier new
        pygame.font.init()
        couriernew = pygame.font.SysFont('couriernew', 24)

        # Text content
        text = self._create_display_text()
        for index in range(len(text)):
            # Text color = (255, 255, 255) = white
            text_surface = couriernew.render(text[index], True, (255, 255, 255))
            text_x = (self._window.get_width() - text_surface.get_width()) / 2
            text_y = (self._window.get_height() / len(text)) * index + (((self._window.get_height() / len(text)) - text_surface.get_height()) / 2)
            self._window.blit(text_surface, (text_x, text_y))

        pygame.display.update()

    def _create_display_text(self):
        """ Gets the end screen text. """
        if int(self._score[1]) == 0:
            text_content = "Sorry, you lose!"
        else:
            text_content = "Congratulations!"
        
        line = "=" * int(self._window.get_width()/14)
        text = [
            line,
            "",
            text_content,
            "",
            f"Items Collected: {self._score[1]}",
            f"Time Remaining: {self._score[2]:.2f}",
            "",
            "Score",
            f"{self._score[0]:.0f}",
            "",
            "Press any key to exit",
            line,
        ]

        return text