#!/usr/bin/python3
"""
given an integer, the function in this module creates
an array of array representing a pascal triangle levels = the integer
"""


def pascal_triangle(n):
    """ creates a pascal triangle of size n """
    lst = []
    if n <= 0:
        return lst

    idx = 0
    while (idx < n):
        i = 0
        child = []
        while (i <= idx):
            if i == 0:
                child.append(1)
            else:
                res = lst[idx - 1][i - 1]
                if i < idx:
                    res += lst[idx - 1][i]
                child.append(res)
            i += 1
        lst.append(child)
        idx += 1

    return lst
