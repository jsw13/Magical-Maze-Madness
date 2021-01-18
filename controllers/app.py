""" This module contains the App class. """

import pygame
import pygame.locals
from models.maze import Maze
from controllers.game_controller import GameController
from controllers.welcome_controller import WelcomeController
from controllers.end_controller import EndController
from models.score import Score
from models.score_manager import ScoreManager
import requests

class App:
    """ Main controller of other game controllers. """
    def __init__(self, height):
        """ Initializes maze object. """
        self._maze = Maze(height, height*2)

    def run(self):
        """ Runs the controllers. """
        # Initiate pygame
        pygame.init()
        # Set window size based on maze dimensions
        y = len(self._maze.maze)*int(600 / len(self._maze.maze))
        x = len(self._maze.maze[0])*int(600 / len(self._maze.maze))
        window = pygame.display.set_mode((x, y))

        score = 0
        running = True
        while running:

            welcome_controller = WelcomeController(self._maze, window)
            welcome_input = welcome_controller.get_user_input()

            if welcome_input == "quit":
                running = False

            if welcome_input == "start":
                time = 10 + 10 * (len(self._maze.maze) // 4)
                game_controller = GameController(self._maze, window, time)
                running = game_controller.get_user_input()

                if running == "finished":
                    score = game_controller.check_score()

                    end_controller = EndController(score, window)
                    running = end_controller.get_user_input()

        pygame.quit()

        try:
            print(f"\nYour score: {score[0]}")

            if score[0] > 0:
                name = input("\nPlease enter your name: ")
                final_score = Score(name, score[0])
                json_score = final_score.to_dict()
                score_manager = ScoreManager()
                score_manager.from_json("scores.json")
                score_manager.add_score(final_score)
                score_manager.to_json("scores.json")

                requests.put("http://localhost:5000/api/new", json=json_score)
            
            print("\nThank you for playing!")
        except:
            print("\nSee you next time")



    
