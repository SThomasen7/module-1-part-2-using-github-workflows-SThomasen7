#!/home/stasen/anaconda3/envs/atms_env/bin/python
import os
import sys
import random
import cells
from getch import getch

def clear_screen():
    """Clear the screen."""
    # disclaimer: AI helped me with this function
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Maze():

    def __init__(self):
        self.maze_size = 16
        self.maze = list()
        self.position = [0, 0]
        for i in range(self.maze_size):
            self.maze.append([""]*self.maze_size)
        self._generate()

    def game_loop(self):
        while True:
            self.draw_screen()
            direction = self.get_input()
            if direction.upper() == 'Q':
                print("Quitting...")
                break
            self.move(direction)

    def get_input(self):
        return getch()

    def move(self, direction):
        direction_map = {
                "W": "N",
                "A": "W",
                "S": "S",
                "D": "E",
                "J": "S",
                "K": "N",
                "H": "W",
                "L": "E"
        }

        if direction.upper() in direction_map:
            direction = direction_map[direction.upper()]

        cell = self._get_cell(self.position)
        if direction.upper() not in cell:
            return

        if direction.upper() == 'N':
            self.position[0]-=1
        if direction.upper() == 'S':
            self.position[0]+=1
        if direction.upper() == 'E':
            self.position[1]+=1
        if direction.upper() == 'W':
            self.position[1]-=1


    def draw_screen(self):
        """draw the maze"""
        clear_screen()
        self._print_header()
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.position[0] == i and self.position[1] == j:
                    cells.print_cell(self.maze[i][j], True)
                else:
                    cells.print_cell(self.maze[i][j], False)
            print("")

    def _generate(self):
        seen = set()
        coord = (0, 0)
        seen.add(coord)
        stack = list()

        def get_unvisited_neighbors(coord):
            neighbors = list()
            if coord[0] != 0:
                neighbors.append((coord[0]-1, coord[1]))
            if coord[0] != self.maze_size-1:
                neighbors.append((coord[0]+1, coord[1]))
            if coord[1] != 0:
                neighbors.append((coord[0], coord[1]-1))
            if coord[1] != self.maze_size-1:
                neighbors.append((coord[0], coord[1]+1))
            unvisited = list()
            for n in neighbors:
                if n not in seen:
                    unvisited.append(n)
            return unvisited
        
        def add_edge(c1, c2):
            if c1[0] - c2[0] == -1:
                self.maze[c1[0]][c1[1]] += "S"
                self.maze[c2[0]][c2[1]] += "N"
            if c1[0] - c2[0] == 1:
                self.maze[c1[0]][c1[1]] += "N"
                self.maze[c2[0]][c2[1]] += "S"
            if c1[1] - c2[1] == -1:
                self.maze[c1[0]][c1[1]] += "E"
                self.maze[c2[0]][c2[1]] += "W"
            if c1[1] - c2[1] == 1:
                self.maze[c1[0]][c1[1]] += "W"
                self.maze[c2[0]][c2[1]] += "E"
            #print(f"{c1}-{c2}  -> {self.maze[c1[0]][c1[1]]}, {self.maze[c2[0]][c2[1]]}")

        while len(seen) < self.maze_size * self.maze_size:

            unvisited = get_unvisited_neighbors(coord)
            
            # if we have no unvisited neighbors, we pop the stack and continue
            if len(unvisited) == 0:
               coord = stack.pop(-1)
               continue

            # get the new coordinate
            new_coord = random.sample(unvisited, 1)[0]
            add_edge(coord, new_coord)
            stack.append(new_coord)
            coord = new_coord
            seen.add(new_coord)
        
    def _get_cell(self, position):
        return self.maze[position[0]][position[1]]

    def _print_header(self):
        print(f"""Welcome to the Maze by Scott Andersen!
Instructions (case insensitive):
Q - quit
W / J - move north        N
A / H - move east       W   E
S / K - move south        S
D / L - move west
Tested on linux! I hope it works on Mac/PC :) 
***
""")

if __name__ == "__main__":
    maze = Maze()
    maze.game_loop()


