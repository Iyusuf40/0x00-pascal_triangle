#!/usr/bin/python3
"""
module contains function that takes in cmd line arg n
and prints the positions n queens would be placed
on a n*n chess board.

APPROACH:
-> chess board is represented as 2-dimensional array
-> however this implementation will represent
   the board as a flattened array by its indeces
   e.g [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
    ]
   will be represented as 0 - 15 to map each position
   to its corresponding index if it were flattend
-> get all possible indeces of the flattened array
-> each index will be called member from now on
-> all possible indeces == n * n - 1
-> virtuallize the 2-dim array or chessboard by
   having functions that compute row and index
   of each member of all_indeces
     - get_index returns index of the member
     - get_row returns row which member belongs
       in the 2-dim array

*** MAJOR ASSUMPTION ***
-> for n number of queens to be placed on the board
   without each having collision path with others means
   each row must have a queen at a position unreachable
   by all other queens
   THEREFORE:
   ALGO:
    -> loop over first row and search for all possible
       members on the later rows that meets the requirement
    -> for each row do as the above
    -> if a row doesnt have a qualified member
       backtrack and continue searching later members of
       the previous row
"""


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

    coexistable = []  # all coexistable queens will be stored here
    all_indeces = (n * n) - 1
    for num in range(n):
        track_recursively(coexistable, num, n, all_indeces)

    for row in coexistable:
        to_print = []
        for num in row:
            row_col_pair = [get_row(num, n), get_index(num, n)]
            to_print.append(row_col_pair)
        print(to_print)
    return coexistable


def track_recursively(global_array, curr_no, length, max_index):
    """ brings main logic together """
    tracker = []
    tracker.append(curr_no)
    # call search_match
    # if successful return tracker from search_match
    # and append to global_array
    # else return none
    search_match(tracker, curr_no, length, max_index, global_array)


def search_match(tracker, curr_no, length, max_index, global_arr):
    """ Implements main logic:
    searches for coexistable queens
    STEPS:
    -> Jumps to next row after the row of curr_no
    -> loops over each member of that row
    -> if member is coexistable with all previous queens
       in tracker array, append member then search next row
       by calling search_match recursively
    -> if in a row no coexistable member is found
    -> backtrack up one level
        - remove the curr_no from tracker array
        - check the next member in the removed member's row
        - continue the search till all members are exhausted
    """
    # go to next row
    # loop over indeces of next row and find match
    # if found append match to tracker and go deeper
    # else backtrack and remove latest appended match
    first_mem_of_next_row = go_to_next_row(curr_no, length)
    first_mem_after_next_row = first_mem_of_next_row + length
    if first_mem_of_next_row > max_index:
        return False

    for num in range(first_mem_of_next_row, first_mem_after_next_row):
        if can_coexist_with_all(tracker, num, length):
            tracker.append(num)
            if len(tracker) == length:
                global_arr.append(tracker[:])
            search_match(tracker, num, length, max_index, global_arr)
            try:
                tracker.pop()
            except Exception:
                pass


def get_index(num, no_of_cols):
    """ returns the computed index of a flattened
    2 dimensional array member
    """
    return num % no_of_cols


def get_row(num, no_of_rows):
    """ returns the computed row of a flattened
    2 dimensional array member
    """
    if num == 0:
        return 0

    return int(num / no_of_rows)  # works like math.floor


def abs(n):
    """ computes absolute value of n """
    if n < 0:
        n = n * -1
    return n


def go_to_next_row(curr_no, length):
    """ returns first index of next row """
    return length * (get_row(curr_no, length) + 1)


def is_in_diagonal_path(curr_no, comp_no, n):
    """ checks if comp_no is in the diagonal
    path of curr_no based on get_index and get_row

    *** LOGIC ***
    -> if the difference between curr_no index
       and comp_no index is equal to the difference
       btwn curr_no and comp_no row then they must
       be in the same diagonal path e.g consider
       this chess board and see the results if it
       members will clash with x diagonally in the
       table below it.
       [
        [y, 0, 0, c, z],
        [0, 0, 0, 0, 0],
        [0, 0, x, 0, 0],
        [0, d, w, 0, 0],
        [a, 0, 0, 0, b],
       ]

        (x)col_diff:row_dif => differences between row and index
        of selected members with compared to x
    member   col     row    (x)col_diff:row_diff  will_clash_diag
      x       2       2              0 : 0             -
      y       0       0              2 : 2            True
      c       3       0              1 : 2            False
      z       4       0              2 : 2            True
      a       0       4              2 : 2            True
      b       4       4              2 : 2            True
      d       1       3              1 : 1            True
      w       2       3              0 : 1            False
    """
    row_diff = abs(get_row(curr_no, n) - get_row(comp_no, n))
    col_diff = abs(get_index(curr_no, n) - get_index(comp_no, n))
    if col_diff == row_diff:
        return True
    return False


def is_in_hor_or_ver_path(curr_no, comp_no, n):
    """ checks if comp_no is in the horizontal or vertical
    path of curr_no based on get_index and get_row
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


def can_coexist_with_all(all_list, comp_no, n):
    """ checks if comp_no is not in a path accessible by
    any number in all_list based on get_index and get_row
    """
    for num in all_list:
        if not can_coexist(num, comp_no, n):
            return False
    return True


if __name__ == "__main__":
    x = main()
    # print(x)
