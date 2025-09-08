#!/home/stasen/anaconda3/envs/atms_env/bin/python
import os

def clear_screen():
    pass

class Maze():

    def __init__(self):
        self.maze_size = 8
        self.maze = list()
        for i in range(self.maze_size):
            self.maze.append([0]*self.maze_size)

    def game_loop(self):
        while not should_exit():
            pass

    def should_exit(self):
        return False

    def get_input(self):
        return False

    def move(self, direction):
        pass

    def draw_screen(self):
        """draw the maze"""
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                print(self.maze[i][j], end="")
            print("")

    def _generate(self):
        pass


if __name__ == "__main__":
    maze = Maze()
    maze.game_loop()

