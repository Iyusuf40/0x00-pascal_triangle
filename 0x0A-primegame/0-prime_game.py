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
    # max_ = max(nums) if nums else 0
    # cache_primes(max_)
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

    if results_cache and results_cache.get(n):
        return results_cache.get(n)

    if n < 2:
        return 'b'

    if n == 2:
        return 'm'

    lst = list(range(2, n + 1))
    first_player = True  # Maria is True while Ben is False
    current_position = 0
    for num in lst:
        if num and (cache.get(num) or is_prime(num)):
            # inner_position = current_position
            # for to_remove in lst[current_position:]:
            #     if to_remove and to_remove % num == 0:
            #         lst[inner_position] = None
            #     inner_position += 1
            first_player = not first_player
        elif num:
            cache[num] = False
        current_position += 1

    if first_player:  # Maria's turn therefore she looses
        results_cache[n] = 'b'
        return 'b'
    results_cache[n] = 'm'
    return 'm'


def is_prime(n):
    """ returns true if n is prime """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if cache.get(n):
        print('hit')
        return True
    if not cache.get(n) and n < cache['max']:
        # print(n, '\nmiss\n')
        return False

    start = 3
    while start < (n ** 0.5) + 1:
        if n % start == 0:
            cache[n] = False
            return False
        start += 2
    if n > cache['max']:
        # print('max set:', n)
        cache['max'] = n
    cache[n] = True
    return True
