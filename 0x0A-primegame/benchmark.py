#!/usr/bin/python3

import time
isWinner = __import__('0-prime_game').isWinner

l3 = [
    [10, [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]
]
ls = list(range(10000))
l4 = [[10000, ls]]


def test(fun, l):
    for x, nums in l:
        # print("Winner: {}\n".format(fun(x, nums)))
        fun(x, nums)
    for x, nums in l:
        # print("Winner: {}\n".format(fun(x, nums)))
        fun(x, nums)
    for x, nums in l:
        # print("Winner: {}\n".format(fun(x, nums)))
        fun(x, nums)
    for x, nums in l:
        # print("Winner: {}\n".format(fun(x, nums)))
        fun(x, nums)

start = time.perf_counter()
test(isWinner, l4)
end = time.perf_counter() - start
print('time:', end)

