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

    for i in range(n):
        child = [1]
        for j in range(i):
            res = 0
            j = j + 1
            res = lst[i - 1][j - 1]
            if j < i:
                res += lst[i - 1][j]
            child.append(res)
        lst.append(child)

    return lst
