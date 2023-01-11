import numpy as np
def add_new(grid):
    empty_cells = np.argwhere(grid == 0)
    if len(empty_cells) > 0:
        cell = empty_cells[np.random.randint(len(empty_cells))]
        if np.random.uniform() < 0.8:
            grid[tuple(cell)] = 2
        else:
            grid[tuple(cell)] = 4
    return grid
