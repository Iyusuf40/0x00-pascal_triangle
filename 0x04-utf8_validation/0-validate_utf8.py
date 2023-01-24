#!/usr/bin/python3
""" module's doc string
Module contains validUTF8 function that validates an array
of data if it is a valid utf8 byte stream

*** Global variables: ***

- top_4_bits: decimal -> 240 Hex -> \xF0 Binary -> 1111 0000
is used to check the first 4 most significant bits if the
character is encoded with 4 bytes.

- top_3_bits, top_2_bits and top_1_bit: LOOK top_4_bits

- blank_4_bytes: decimal -> 8 Hex -> \x08 Binary -> 0000 1000
is used to ensure the immediate bit after top_4_bits is 0
as this is the convention for utf8 encoding ie first byte
must be 11110xxx pattern. Link:
https://en.wikipedia.org/wiki/UTF-8#Encoding

- blank_3_bytes, blank_2_bytes, blank_1_byte: LOOK blank_4_bytes

*** functions ***

- validUTF8: [Boolean]
[x] if len(data) == 1 -> checks if data stream contains only 1 byte
since a byte can only be used to store ASCII characters,
it must be between 0 and 127, boundaries inclusive.

[x] otherwise data contains multiple bytes

<-- while loop -->
FOR EACH BYTE

[x] if byte > 127 -> checks if byte can be represented with only
7 bits, as such it must be an ASCII character

[x] otherwise byte must be the start of a multibyte encoding.
Therefore, use the top_x_bits mask to check the number of
bytes used to encode character and blank_x_bytes to check and ensure
immediately following bit is 0.

If valid shift index x number of times


- check_continuation_bytes: [Boolean]
checks the following bytes of a multibyte character and validates
it that they all start with 10xxxxxx bits.
"""


top_4_bits = 240
blank_4_bytes = 8

top_3_bits = 224
blank_3_bytes = 16

top_2_bits = 192
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
        if byte > 255:  # integer is represented by more than 1 byte
            byte = (byte ^ 256) & 255  # get first byte
        if byte > 127:
            if top_4_bits ^ byte < 16 and not blank_4_bytes & byte:
                if check_continuation_bytes(data, 3, index):
                    index += 4
                else:
                    return False
            elif top_3_bits ^ byte < 32 and not blank_3_bytes & byte:
                if check_continuation_bytes(data, 2, index):
                    index += 3
                else:
                    return False
            elif top_2_bits ^ byte < 64 and not blank_2_bytes & byte:
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
    if end > len(data):  # will raise index error
        return False
    while index < end:
        if data[index] & top_1_bit and not data[index] & blank_1_byte:
            index += 1
        else:
            return False
    return True
