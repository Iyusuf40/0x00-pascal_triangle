#!/bin/python3


island_prm = __import__("0-island_perimeter").island_perimeter
import time

def island_perimeter_v(grid):
    """
    calculates the total perimeter
    of an Island
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += check_rt_lt(grid, i, j)
                perimeter += check_tp_dn(grid, i, j)
    return perimeter


def check_rt_lt(grid, i, j):
    """
    checks the left and right side of
    the grid
    """
    perimeter = 0
    if (j + 1) > (len(grid[i]) - 1) or grid[i][j + 1] == 0:
        perimeter += 1
    if (j - 1) < 0 or grid[i][j - 1] == 0:
        perimeter += 1
    return perimeter


def check_tp_dn(grid, i, j):
    """
    check the top and bottom side of
    the grid
    """
    perimeter = 0
    if (i - 1) < 0 or grid[i - 1][j] == 0:
        perimeter += 1
    if (i + 1) > (len(grid) - 1) or grid[i + 1][j] == 0:
        perimeter += 1
    return perimeter

def island_perimeter(grid):
    """checks for cells in a grid that contains 1
    each cell with 1 is considered land amidst water ie 0s,
    returns the perimeter of on island"""

    prev_row = 0
    next_row = 0
    prev_index = 0
    next_index = 0
    max_row_length = len(grid[0])
    grid_height = len(grid)
    current_index = 0
    row_index = 0
    perimeter = 0
    while row_index < grid_height:
        current_index = 0
        while current_index < max_row_length:
            current = grid[row_index][current_index]
            if current:
                prev_index = current_index - 1
                if prev_index > -1 and not grid[row_index][prev_index]:
                    perimeter += 1
                next_index = current_index + 1
                if next_index < max_row_length and not \
                        grid[row_index][next_index]:
                    perimeter += 1
                prev_row = row_index - 1
                if prev_row > -1 and not grid[prev_row][current_index]:
                    perimeter += 1
                next_row = row_index + 1
                if next_row < grid_height and not \
                        grid[next_row][current_index]:
                    perimeter += 1

                if prev_index < 0:
                    if prev_row < 0:
                        perimeter += 2
                    elif next_row == grid_height:
                        perimeter += 2
                    else:
                        perimeter += 1
                if next_index == max_row_length:
                    if prev_row < 0:
                        perimeter += 2
                    elif next_row == grid_height:
                        perimeter += 2
                    else:
                        perimeter += 1

                if prev_row < 0 or next_row == grid_height:
                    if prev_index > -1 and next_index < max_row_length:
                        perimeter += 1

            current_index += 1
        row_index += 1

    return perimeter


def create_island_sqaure_of_side_x(x):
    parent = []
    for row in range(x):
        child = [0]
        child.extend([1 for i in range(x)])
        child.append(0)
        parent.append(child)
    return parent


def grid_print(grid):
    print("[")
    for row in grid:
        print(f"  {row},")
    print("]")


if __name__ == "__main__":
    grid = create_island_sqaure_of_side_x(250)
    # grid_print(grid)
    start = time.perf_counter()
    print(island_prm(grid))
    # print(island_perimeter_v(grid))
    # print(island_perimeter(grid))
    end = time.perf_counter() - start
    print(end)
