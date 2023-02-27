#!/usr/bin/python3
""" Island perimeter solution"""


def island_perimeter(grid):
    """ computes and return the perimeter of island in grid """
    sum = 0
    if not grid:
        return sum

    width = len(grid[0])
    height = len(grid)

    start_position = get_first_wall(grid, height, width)
    if not start_position:
        return sum
    start_row, start_col = start_position

    first_square_prm = get_first_square_prm(grid, start_row, start_col, width)
    return first_square_prm

    return sum


def get_first_wall(grid, height, width):
    """searches for first wall and returns its position """
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col]:
                return start_row, start_col
    
    return None


def check_walls(grid, start_row, start_col, height, width):
    """ walks along walls and counts each square face """
    prev_row = start_row - 1 if start_row else 0
    prev_col = start_col - 1 if start_col else 0
    # top = 0
    # right = 0
    left = 0
    # if start_row:
    #     if start_col:
    #         top = grid[start_row - 1][start_col - 1]
    # if start_col:
    #     right = grid[start_row][start_col - 1]
    if width > start_col:
        left = grid[start_row][start_col + 1]
    
    if left:
        sum = 2
    next_row = start_row + 1
    next_col = start_col + 1


def get_first_square_prm(grid, start_row, start_col, width):
    """ computes the perimeter of 1st square """
    perimeter = 3
    left = 0
    if width > start_col:
        left = grid[start_row][start_col + 1]
    
    if left:
        perimeter = 2
    
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
