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

    for row in coexistable:
        to_print = []
        for index in range(len(row)):
            num = row[index]
            row_col_pair = [get_row(num, n), get_index(num, n)]
            to_print.append(row_col_pair)
        print(to_print)
    return coexistable


def track_recursively(global_array, curr_no, length, max_index):
    """ implements main logic """
    tracker = []
    tracker.append(curr_no)
    # call search_match
    # if successful return tracker from search_match
    # and append to global_array
    # else return none
    res = search_match(tracker, curr_no, length, max_index)
    if res:
        global_array.append(res)
    else:
        return


def search_match(tracker, curr_no, length, max_index):
    """ searches for coexistable quuens """
    # go to next row
    # loop over indeces of next row and find match
    # if found append match to tracker and go deeper
    # else backtrack and remove latest appended match
    first_mem_of_next_row = go_to_next_row(curr_no, length)
    last_mem_of_next_row = first_mem_of_next_row + length
    for num in range(first_mem_of_next_row, last_mem_of_next_row):
        if can_coexist_with_all(tracker, num, length):
            tracker.append(num)
            if len(tracker) == length:
                return tracker
            res = search_match(tracker, num, length, max_index)
            if res:
                return res
            else:
                tracker.pop()
    return None


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
    # print(can_coexist(1, 15, 4))
