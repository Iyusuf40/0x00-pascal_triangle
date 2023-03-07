#!/usr/bin/python3
"""mod doc's"""

cache = {'max': 3, 2: True, 3: True}
results_cache = {}


def cache_primes(n):
    """ creates a cache of primes """
    if n <= cache['max']:
        return
    for x in range(cache['max'], n + 1):
        if is_prime(x):
            cache[x] = True


def isWinner(x, nums):
    """ determines  who wins """
    Maria = 0
    Ben = 0

    if (
        not x or not nums or type(x) is not int
        or type(nums) is not list or x > len(nums)
    ):
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

    if results_cache.get(n):
        return results_cache.get(n)

    if n < 2:
        return 'b'

    if n == 2:
        return 'm'

    player = True  # Maria is True while Ben is False
    for num in range(2, n + 1):
        if cache.get(num) or is_prime(num):
            player = not player

    if player:  # Maria's turn therefore she looses
        results_cache[n] = 'b'
        return 'b'
    results_cache[n] = 'm'
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
        # print(n, '\nmiss\n')
        return False

    start = 3
    end = int(n ** 0.5) + 1
    while start < end:
        if n % start == 0:
            cache[n] = False
            return False
        start += 2
    if n > cache['max']:
        # print('max set:', n)
        cache['max'] = n
    cache[n] = True
    return True
