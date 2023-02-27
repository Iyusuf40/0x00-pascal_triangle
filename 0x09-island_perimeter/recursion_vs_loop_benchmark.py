#!/bin/python3


island_prm_loop = __import__("0-island_perimeter").island_perimeter
island_prm_rcs = __import__("0-island_perimeter_recursive").island_perimeter
import time
import sys


sys.setrecursionlimit(30000)


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
    grid = create_island_sqaure_of_side_x(4000)
    # grid_print(grid)
    print()
    start = time.perf_counter()
    print(island_prm_loop(grid), 'yusuf loop')
    end = time.perf_counter() - start
    print(end)
    print()

    start = time.perf_counter()
    print(island_prm_rcs(grid), 'yusuf recursive')
    end = time.perf_counter() - start
    print(end)
    print()
