#!/bin/python3


island_prm = __import__("0-island_perimeter").island_perimeter


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
    grid = [[0, 1, 1, 0], [0, 1, 1, 0]]
    print(island_prm(grid))
    grid = create_island_sqaure_of_side_x(200)
    # grid_print(grid)
    print(island_prm(grid))
