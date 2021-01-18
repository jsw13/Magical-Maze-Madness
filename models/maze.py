""" This module contains the Maze class. """
from models.player import Player
from models.maze_gen import MazeGen
import random

class Maze:
    """ Represents the maze in our game. """
    def __init__(self, height, width):
        # self._maze = self._load_maze(filename)
        self._maze_gen = MazeGen(height, width)
        self._maze = self.random_maze()
        self._exit = self._find_exit()
        self._player = Player()

    def random_maze(self):
        random_maze = self._maze_gen.random_maze
        return random_maze

    def _load_maze(self, filename):
        """ Loads maze information from a txt file. 
        
        Args:
            filename (str): filename to load maze from

        Returns:
            maze (list): maze information stored in a list

        Raises:
            ValueError: if file cannot be opened
        """
        try:
            with open(filename, "r") as f:
                lines = f.read().splitlines()
                self._maze = [[i for i in row] for row in lines]
                return self._maze
        except:
            raise ValueError(f"Could not read {filename}.")

    @property
    def maze(self):
        """ Returns the maze attribute. """
        return self._maze

    def _find_exit(self):
        """ Finds the location of the exit in the maze. 
        
        Returns:
            tuple: contains row number and column number of exit.
        """
        for row_index,row in enumerate(self._maze):
            for column_index in range(len(row)):
                if self._maze[row_index][column_index] == "E":
                    # The exit is now a space, not an unpassable block
                    self._maze[row_index][column_index] = " "
                    self._exit = (row_index, column_index)
                    return self._exit

    def can_move_to(self, row_number, column_number):
        """ Checks whether space in maze is wall or can move to. 
        
        Args:
            location (tuple): contains row number (int) and column number (int)

        Returns:
            bool: True if space can be moved to. False if space cannot be moved to.
        """
        if self._maze[row_number][column_number] in ["X", "E"]:
            return False
        else:
            return True

    def get_player_location(self):
        """ Returns the row number and column number of player location in a tuple. """
        for row_index,row in enumerate(self._maze):
            for column_index in range(len(row)):
                if self._maze[row_index][column_index] == "P":
                    location = (row_index, column_index)
                    return location

    def is_exit(self):
        """ Returns True if the player is on the exit and player has at least 3 items collected. """
        location = self.get_player_location()
        items_collected = len(self._player.collection)
        if (location == self._exit and items_collected > 2):
            return True
        else:
            return False

    def find_random_spot(self):
        """ Randomly selects an empty " " space in maze.
        
        Returns:
            tuple (int, int): contains row number and column number of random spot
        """
        empty_spaces = []
        for row_index,row in enumerate(self._maze):
            for column_index in range(len(row)):
                if self._maze[row_index][column_index] == " ":
                    empty_tuple = (row_index, column_index)
                    empty_spaces.append(empty_tuple)

        random_number = random.randint(0,len(empty_spaces)-1)
        random_spot = empty_spaces[random_number]

        return random_spot

    def add_items(self):
        """ Adds 5 items to a 5 random empty space on the maze."""
        items = ["a", "b", "c", "d", "e"]
        for item in items:
            random_spot = self.find_random_spot()
            self._maze[random_spot[0]][random_spot[1]] = item

    def move_player(self, vertical, horizontal):
        """ Moves the player to a new location in the maze. """
        location = self.get_player_location()
        row_number = location[0]
        column_number = location[1]

        if (row_number + vertical) < 0:
            row_number = 0
        elif (row_number + vertical) > (len(self._maze) - 1):
            row_number = (len(self._maze) - 1)
        else:
            row_number += vertical

        if (column_number + horizontal) < 0:
            column_number = 0
        elif (column_number + horizontal) > (len(self._maze[0]) -1):
            column_number = (len(self._maze[0]) - 1)
        else:
            column_number += horizontal
        
        if self.can_move_to(row_number, column_number):
            self.check_item(row_number, column_number)
            self._maze[location[0]][location[1]] = " "
            self._maze[row_number][column_number] = "P"

    def check_item(self, row_number, column_number):
        """ Checks if an item is in a location. Player collects item if item is in location. """
        if self._maze[row_number][column_number] not in [" ", "P", "Q", "X"]:
            item = self._maze[row_number][column_number]
            self._player.collect_item(item)

    def items_remaining(self):
        """ Returns the number of items remaining in the maze. """
        items_remaining = 5 - len(self._player.collection)
        return items_remaining

    def open_exit(self):
        """ Changes the exit marker when player collects enough items. """
        if len(self._player.collection) > 2:
            self._maze[self._exit[0]][self._exit[1]] = "Q" 