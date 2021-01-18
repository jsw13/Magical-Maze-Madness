""" This modules contains the GameView class. """
import pygame
import pygame.locals
import os
import random

class GameView:
    """ Displays the maze and objects in the maze. """ 

    WALL = [
        "witch_wall.png", 
        "wall1.png",
        "wall2.png",
        "wall3.png",
        "wall4.png",
        "wall5.png",
        "wall6.png",
        "wall7.png",
        "wall8.png",
        "wall9.png",
        "wall10.png",
        "wall11.png",
        "wall12.png",
        "wall13.png",
        "wall4.png",
        "wall15.png",
        "wall16.png",
        "wall17.png"
    ]

    def __init__(self, maze, window):
        """ Initializes the private attribute maze.

        Args:
            maze (list): list containing the maze and objects in the maze
        """
        self._maze = maze
        self._window = window

        self._theme = random.randint(0, len(self.WALL)-1)
        self._wall = self.WALL[self._theme]

    def display_maze(self, time, direction):
        """ Prints the maze to the display. """
        # background color
        self._window.fill((15,11,24))

        # tile width and height, calculated from window size and maze
        tile_x = int(self._window.get_width() / len(self._maze[0]))
        tile_y = tile_x

        wall_image = pygame.image.load(os.path.join("images", self._wall))
        wall = pygame.transform.scale(wall_image, (tile_x, tile_y))

        path = pygame.Surface((tile_x,tile_y))
        path.fill((15,11,24))
        # path_image = pygame.image.load(os.path.join("images", self._path))
        # path = pygame.transform.scale(path_image, (tile_x, tile_y))

        player_image = ""
        if direction == "up":
            player_image = pygame.image.load(os.path.join("images", "witch_up.png"))
        if direction == "down":
            player_image = pygame.image.load(os.path.join("images", "witch_down.png"))
        if direction == "left":
            player_image = pygame.image.load(os.path.join("images", "witch_left.png"))
        if direction == "right":
            player_image = pygame.image.load(os.path.join("images", "witch_right.png"))
        player = pygame.transform.scale(player_image, (tile_x, tile_y))
        

        # entrance_image = pygame.image.load(os.path.join("images", "entrance.png"))
        # entrance = pygame.transform.scale(entrance_image, (tile_x, tile_y))

        exit_image = pygame.image.load(os.path.join("images", "witch_exit.png"))
        exit = pygame.transform.scale(exit_image, (tile_x, tile_y))

        # closed_exit_image = pygame.image.load(os.path.join("images", "closed_exit.png"))
        # closed_exit = pygame.transform.scale(closed_exit_image, (tile_x, tile_y))

        item1_image = pygame.image.load(os.path.join("images", "witch_item1.png"))
        item1 = pygame.transform.scale(item1_image, (tile_x, tile_y))
        item2_image = pygame.image.load(os.path.join("images", "witch_item2.png"))
        item2 = pygame.transform.scale(item2_image, (tile_x, tile_y))
        item3_image = pygame.image.load(os.path.join("images", "witch_item3.png"))
        item3 = pygame.transform.scale(item3_image, (tile_x, tile_y))
        item4_image = pygame.image.load(os.path.join("images", "witch_item4.png"))
        item4 = pygame.transform.scale(item4_image, (tile_x, tile_y))
        item5_image = pygame.image.load(os.path.join("images", "witch_item5.png"))
        item5 = pygame.transform.scale(item5_image, (tile_x, tile_y))


        for row in range(len(self._maze)):
            for column in range(len(self._maze[row])):
                if self._maze[row][column] == "P":
                    self._window.blit(player, (column*tile_x, row*tile_y))
                if self._maze[row][column] == "E":
                    self._window.blit(exit, (column*tile_x, row*tile_y))
                if self._maze[row][column] == "Q":
                    self._window.blit(exit, (column*tile_x, row*tile_y))
                if self._maze[row][column] == "X":
                    self._window.blit(wall, (column*tile_x, row*tile_y))
                if self._maze[row][column] == " ":
                    self._window.blit(path, (column*tile_x, row*tile_y))
                if self._maze[row][column] in "a":
                    self._window.blit(item1, (column*tile_x, row*tile_y))
                if self._maze[row][column] in "b":
                    self._window.blit(item2, (column*tile_x, row*tile_y))
                if self._maze[row][column] in "c":
                    self._window.blit(item3, (column*tile_x, row*tile_y))
                if self._maze[row][column] in "d":
                    self._window.blit(item4, (column*tile_x, row*tile_y))
                if self._maze[row][column] in "e":
                    self._window.blit(item5, (column*tile_x, row*tile_y))

        pygame.font.init()
        couriernew = pygame.font.SysFont('couriernew', 24, bold=True)
        time_surface = couriernew.render(f"{time:.2f}", True, (0, 255, 0))
        self._window.blit(time_surface, (10, 10))

        pygame.display.update()

