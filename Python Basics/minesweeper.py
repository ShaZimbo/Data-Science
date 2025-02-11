""" This program generates a random grid of hashes and minesweeper numbers. """
import random


def make_grid(width, hight):
    """ Create a grid of specified dimensions. """
    return [["-" for _ in range(width)] for _ in range(hight)]


def grid(width, hight, max_hash):
    """ Create a grid with a random number of hashes. """
    new_grid = make_grid(width, hight)
    for h in range(hight):
        num_hash = random.randint(1, max_hash)
        hash_pos = random.sample(range(width), num_hash)

        for w in hash_pos:
            new_grid[h][w] = "#"
    return new_grid


# Function to identify relational positions
def get_surrounding_positions(grid_data, r, col):
    """ Return the positions of surrounding cells. """
    positions = {
        "nw": grid_data[r - 1][col - 1]
        if r > 0 and col > 0 else None,
        "n": grid_data[r - 1][col]
        if r > 0 else None,
        "ne": grid_data[r - 1][col + 1]
        if r > 0 and col < len(grid_data[0]) - 1 else None,
        "w": grid_data[r][col - 1]
        if col > 0 else None,
        "center": grid_data[r][col],
        "e": grid_data[r][col + 1]
        if col < len(grid_data[0]) - 1 else None,
        "sw": grid_data[r + 1][col - 1]
        if r < len(grid_data) - 1 and col > 0 else None,
        "s": grid_data[r + 1][col]
        if r < len(grid_data) - 1 else None,
        "se": grid_data[r + 1][col + 1]
        if r < len(grid_data) - 1 and col < len(grid_data[0]) - 1 else None
    }
    return positions


# Set dimensions of grid and number of hashes
random_grid = grid(15, 15, 5)

# Check rows in grid
for row_index, row in enumerate(random_grid):
    # Check cells in each row
    for col_index, cell in enumerate(row):
        # if there is no mine in cell
        if cell != "#":
            MINES = 0
            surrounding_positions = get_surrounding_positions(
                random_grid, row_index, col_index)
            # Add 1 for each # in surrounding cells
            for _ in surrounding_positions.values():
                if _ == "#":
                    MINES += 1
            random_grid[row_index][col_index] = str(MINES)
for row in random_grid:
    print(" ".join(row))
