#!/usr/bin/python3
"""Maria and Ben are playing a game. Given
a set of consecutive integers starting from 1
up to and including n, they take turns choosing
a prime number from the set and removing that
number and its multiples from the set.
The player that cannot make a move loses the game
"""

cache = {'max': 3, 2: True, 3: True}


def cache_primes(n):
    """ creates a cache of primes """
    if n <= cache['max']:
        return
    for x in range(cache['max'], n + 1):
        if is_prime(x):
            cache[x] = True
            cache['max'] = x


def isWinner(x, nums):
    """ determines  who wins """
    Maria = 0
    Ben = 0

    cache_primes(max(nums))

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
    if n < 2:
        return 'b'

    if n == 2:
        return 'm'

    player = True  # Maria is True while Ben is False
    for num in range(2, n + 1):
        if cache.get(num):
            player = not player

    if player:  # Maria's turn therefore she looses
        return 'b'
    return 'm'


def is_prime(n):
    """ returns true if n is prime """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if cache.get(n):
        return True
    if not cache.get(n) and n < cache['max']:
        return False

    start = 3
    end = int(n ** 0.5) + 1
    while start < end:
        if n % start == 0:
            return False
        start += 2
    if n > cache['max']:
        cache['max'] = n
    cache[n] = True
    return True
