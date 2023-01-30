#!/usr/bin/python3


import sys


def main():
    """ main function """
    n = 0
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    coexistable = []
    all_indeces = (n * n) - 1
    for num in range(n):
        track_recursively(coexistable, num, n, all_indeces)

    return coexistable


def track_recursively(global_array, curr_no, length, max_index):
    """ implements main logic """
    pass


def get_index(num, no_of_cols):
    """ returns the computed index of a flattened
    2 dimensional array
    """
    return num % no_of_cols


def get_row(num, no_of_rows):
    """ returns the computed row of a flattened
    2 dimensional array
    """
    if num == 0:
        return 0

    return int(num / no_of_rows)  # works like math.floor


def abs(n):
    """ computes absolute vslue of n """
    if n < 0:
        n = n * -1
    return n


def go_to_next_row(curr_no, length):
    """ returns first index of next row """
    return length * (get_row(curr_no, length) + 1)


def is_in_diagonal_path(curr_no, comp_no, n):
    """ checks if compared_no is in the diagonal
    path of current_no based on get_index and get_row
    """
    row_diff = abs(get_row(curr_no, n) - get_row(comp_no, n))
    col_diff = abs(get_index(curr_no, n) - get_index(comp_no, n))
    if col_diff == row_diff:
        return True
    return False


def is_in_hor_or_ver_path(curr_no, comp_no, n):
    """ checks if compared_no is in the horizontal or vertical
    path of current_no based on get_index and get_row
    """
    if get_index(curr_no, n) == get_index(comp_no, n):
        return True
    if get_row(curr_no, n) == get_row(comp_no, n):
        return True
    return False


def can_coexist(curr_no, comp_no, n):
    """ checks if compared_no is not in a path accessible by
    curr_no path of current_no based on get_index and get_row
    """
    if is_in_hor_or_ver_path(curr_no, comp_no, n):
        return False
    if is_in_diagonal_path(curr_no, comp_no, n):
        return False
    return True


if __name__ == "__main__":
    main()
    print(can_coexist(1, 15, 4))
