#!/usr/bin/python3
""" module's doc string """


top_4_bits = 240
blank_4_bytes = 8

top_3_bits = 224
blank_3_bytes = 16

top_2_bits = 208
blank_2_bytes = 32

top_1_bit = 128
blank_1_byte = 64


def validUTF8(data):
    """  determines if a given data set represents a valid UTF-8 encoding """

    index = 0

    if len(data) == 1:
        return data[0] < 128 and data[0] >= 0

    while index < len(data):
        byte = data[index]
        if byte > 127:
            if top_4_bits ^ byte < top_4_bits and not blank_4_bytes & byte:
                if check_continuation_bytes(data, 3, index):
                    index += 4
                else:
                    return False
            elif top_3_bits ^ byte < top_3_bits and not blank_3_bytes & byte:
                if check_continuation_bytes(data, 2, index):
                    index += 3
                else:
                    return False
            elif top_2_bits ^ byte < top_2_bits and not blank_2_bytes & byte:
                if check_continuation_bytes(data, 1, index):
                    index += 2
                else:
                    return False
            elif top_1_bit & byte:
                return False
        else:
            index += 1
    return True


def check_continuation_bytes(data, no_of_continuation_bytes, current_index):
    """ checks if continuation bytes are valid """
    index = current_index + 1
    end = index + no_of_continuation_bytes
    while index < end:
        if data[index] & top_1_bit and not data[index] & blank_1_byte:
            index += 1
        else:
            return False
    return True
