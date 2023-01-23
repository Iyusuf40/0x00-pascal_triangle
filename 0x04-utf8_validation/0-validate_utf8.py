#!/usr/bin/python3
""" module's doc string """


def validUTF8(data):
    """  determines if a given data set represents a valid UTF-8 encoding """
    for item in data:
        if item > 127 or item < 0:
            return False
    return True
