import random

class MazeGen():
    def __init__(self, height, width):
        self._maze = self.maze_init(height, width)
        self._location = [0, 0]
        self._move_list = []

    def maze_init(self, height, width):
        if type(width) is not int and type(height) is not int:
            raise TypeError
        if height % 2 == 0:
            height = height + 1
        if width % 2 == 0:
            width = width + 1

        maze = []
        for i in range(height):
            maze_row = []
            for j in range(width):
                maze_row.append("X")
            maze.append(maze_row)
        maze[0][0] = "P"

        return maze

    def print_maze(self):
        for row in self._maze:
            print_row = ""
            for column in row:
                print_row += column
            print(print_row)

    def move(self, dx, dy):
        x = self._location[0]
        y = self._location[1]

        if (x + dx) < len(self._maze) and (x + dx) >= 0 and (y + dy) >= 0 and (y + dy) < len(self._maze[x]):
            if self._maze[x + int(dx/2)][y + int(dy/2)] == "X" and self._maze[x + dx][y + dy] == "X":
                self._maze[x + int(dx/2)][y + int(dy/2)] = " "
                self._maze[x + dx][y + dy] = " "
                self._location = [x + dx, y + dy]
                self._move_list.append((dx, dy))
                return True
            else:
                return False
        else:
            return False

    def reverse(self):
        reverse = True
        while reverse:
            x = self._location[0]
            y = self._location[1]
            last_move = self._move_list[-1]
            second_last_move = self._move_list[-2]

            if last_move == second_last_move:
                reverse = True
            else:
                reverse = False

            self._location = [x - last_move[0], y - last_move[1]]
            self._move_list.pop()

        return False

    def clear_forward(self, open_moves=[[2, 0], [-2, 0], [0, 2], [0, -2]]):

        clear = True
        while clear:
            if len(open_moves) == 0:
                clear = False
                return clear
            
            direction = random.randint(0,len(open_moves)-1)
            
            move = self.move(open_moves[direction][0], open_moves[direction][1])
            if not move:
                open_moves.pop(direction)
                self.clear_forward(open_moves)
            else:
                self.clear_forward([[2, 0], [-2, 0], [0, 2], [0, -2]])
            
            clear = move
            
        return False

    def make_maze(self):

        finished = False
        while finished == False:
            clear = self.clear_forward([[2, 0], [-2, 0], [0, 2], [0, -2]])
            try:
                if clear == False:
                    finished = self.reverse()
            except:
                finished = True
        
        self._maze[len(self._maze)-1][len(self._maze[0])-1] = "E"

    @property
    def random_maze(self):
        self.make_maze()
        return self._maze

if __name__ == "__main__":
    maze = MazeGen(11, 21)