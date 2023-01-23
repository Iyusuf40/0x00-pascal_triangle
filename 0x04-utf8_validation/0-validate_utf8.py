#!/usr/bin/python3
""" module's doc string """


top_four_bits = 240
blank_four_bytes = 8

top_three_bits = 224
blank_three_bytes = 16

top_two_bits = 208
blank_two_bytes = 32

top_one_bit = 128
blank_one_byte = 64


def validUTF8(data):
    """  determines if a given data set represents a valid UTF-8 encoding """

    index = 0

    if len(data) == 1:
        return data[0] < 128 and data[0] >= 0

    while  index < len(data):
        byte = data[index]
        if top_four_bits & byte and not blank_four_bytes & byte:
            print("enterd")
            if check_continuation_bytes(data, 3, index):
                index += 4
            else:
                return False
        elif top_three_bits & byte and not blank_three_bytes & byte:
            if check_continuation_bytes(data, 2, index):
                index += 3
            else:
                return False
        elif top_two_bits & byte and not blank_two_bytes & byte:
            if check_continuation_bytes(data, 1, index):
                index += 2
            else:
                return False
        elif top_one_bit & byte:
            return False
        else:
            index += 1
    return True


def check_continuation_bytes(data, no_of_continuation_bytes, current_index):
    """ checks if continuation bytes are valid """
    index = current_index + 1
    end = index + no_of_continuation_bytes
    while index < end:
        if data[index] & top_one_bit and not data[index] & blank_one_byte:
            index += 1
        else:
            return False
    return True
