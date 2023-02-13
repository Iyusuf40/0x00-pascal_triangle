#!/usr/bin/python3
""" mod doc string """


def rotate_2d_matrix(m):
    """main function: rotates a 2d array 90 deg"""
    width = len(m[0])
    height = len(m)
    total_items = width * height
    map_ = build_map(m, total_items, width)
    # print(map_)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, index = compute_row_and_index(new_index, width)
        m[row][index] = value


def build_map(m, length, width):
    """returns a map of prev_index and their
    next positions"""
    dct = {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }
    return dct


def get_new_index(i, width):
    """computes new position"""
    current_index = i % width
    current_row = int(i / width)
    next_index = width - 1 - current_row
    next_row = current_index
    next_position = next_row * width + next_index
    return next_position


def get_value(m, i, width):
    """gets the value of a 2d array by denormalizing
    its flattened index"""
    current_index = i % width
    current_row = int(i / width)
    return m[current_row][current_index]


def compute_row_and_index(flat_index, width):
    """returns denormalized row and index from a
    flattened 2d array index"""
    row = int(flat_index / width)
    index = flat_index % width
    return row, index


def printx(lst):
    print("[")
    for itm in lst:
        print("  ", str(itm) + ",")
    print("]")


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    rotate_2d_matrix(matrix)
    printx(matrix)
