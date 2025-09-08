#!/bin/python3
"""Maze game."""
import os
import random
import cells
from getch import getch


def clear_screen():
    """Clear the screen."""
    # Disclaimer: AI helped me with this function
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Maze():
    """Maze class, creates maze instance and runs game."""

    def __init__(self):
        """Initialize the maze class."""
        self.maze_size = 16
        self.maze = list()
        self.position = [0, 0]
        for i in range(self.maze_size):
            self.maze.append([""]*self.maze_size)
        self._generate()

    def game_loop(self):
        """Run the game loop."""
        direction = ""
        # Infinite loop for the game loop, we break out with breaks.
        while True:

            # Check if the maze has been escaped.
            if self.position[0] == self.maze_size-1 and \
                    self.position[1] == self.maze_size:
                print("You've escaped the maze!!")
                break

            # Redraw the screen.
            self.draw_screen()
            print("Previous move: ", direction)

            # Get the next move, quit if the user inputs 'Q'.
            direction = self.get_input()
            if direction.upper() == 'Q':
                print("Quitting...")
                break
            self.move(direction)

    def get_input(self):
        """Get user input."""
        return getch()

    def move(self, direction):
        """Move the current position."""
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

        # Map keypress to a direction.
        if direction.upper() in direction_map:
            direction = direction_map[direction.upper()]

        # Check if that move is valid for the current cell.
        cell = self._get_cell(self.position)
        if direction.upper() not in cell:
            return

        # Adjust the position based on the keypress.
        if direction.upper() == 'N':
            self.position[0] -= 1
        if direction.upper() == 'S':
            self.position[0] += 1
        if direction.upper() == 'E':
            self.position[1] += 1
        if direction.upper() == 'W':
            self.position[1] -= 1

    def draw_screen(self):
        """Draw the maze."""
        clear_screen()
        self._print_header()

        # Print the maze cells, highlight if we are in that position.
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.position[0] == i and self.position[1] == j:
                    cells.print_cell(self.maze[i][j], True)
                else:
                    cells.print_cell(self.maze[i][j], False)
            if i == self.maze_size - 1:
                print(" <- EXIT")
            else:
                print("")

    def _generate(self):
        """Generate the maze."""
        seen = set()
        coord = (0, 0)
        seen.add(coord)
        stack = list()

        # Helper functions.
        def get_unvisited_neighbors(coord):
            """Get unvisited neighbors for the given cell."""
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
            """Add an edge to the maze."""
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
            # print(f"{c1}-{c2}  -> ", "
            #   {self.maze[c1[0]][c1[1]]}, {self.maze[c2[0]][c2[1]]}")

        # Until we have visited all of the cells, keep visiting.
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

        # after the maze is generated add the exit position
        self.maze[self.maze_size-1][self.maze_size-1] += 'E'

    def _get_cell(self, position):
        """Get the maze cell at the position."""
        return self.maze[position[0]][position[1]]

    def _print_header(self):
        """Print the screen header."""
        print("""Welcome to the Maze by Scott Andersen!
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
