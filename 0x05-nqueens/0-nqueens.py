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


if __name__ == "__main__":
    main()
    print(go_to_next_row(4, 4))
