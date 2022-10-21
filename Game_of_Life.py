#implementing Conway's Game of Life
from collections import namedtuple
Cell = namedtuple("Cell", ["row", "column"])

"""A class implementing a Game_of_Life grid"""
class Grid:
    offsets = [(-1,0), (1,0), (0,1), (0,-1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    def __init__(self, r, c, alive_cells = {}):
        self.alive_cells = alive_cells
        self.rows = r
        self.columns = c
    
    def evolve(self):
        next_alive = set(self.alive_cells)
        for row in range(self.rows):
            for col in range(self.columns):
                current_cell = Cell(row, col)
                alive, dead = get_neighbours(self, current_cell)
                if current_cell in self.alive_cells:
                    if alive < 2 or alive > 3:
                        next_alive.remove(current_cell)
                else:
                    if alive == 3:
                        next_alive.add(current_cell)
        return next_alive
