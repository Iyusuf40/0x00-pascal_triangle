#!/usr/bin/python3
"""mod doc's"""


def isWinner(x, nums):
    """ determines  who wins """
    Maria = 0
    Ben = 0

    if not x or not nums or x < 1:
        return None
    for index in range(x):
        n = nums[index]
        winner = getWinner(n)
        if winner == 'm':
            Maria += 1
        elif winner == 'b':
            Ben += 1
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    return None


def getWinner(n):
    """ checks for prime """

    if n < 1:
        return None
    if n < 2:
        return 'b'

    lst = list(range(2, n + 1))
    first_player = True  # Maria is True while Ben is False
    current_position = 0
    for num in lst:
        if num and is_prime(num):
            inner_position = current_position
            for to_remove in lst[current_position:]:
                if to_remove and to_remove % num == 0:
                    lst[inner_position] = None
                inner_position += 1
            first_player = not first_player
        current_position += 1
    if first_player:  # Maria's turn therefore she looses
        return 'b'
    return 'm'


def is_prime(n):
    """ returns true if n is prime """
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    start = 3
    while start < (n ** 0.5) + 1:
        if n % start == 0:
            return False
        start += 2
    return True
