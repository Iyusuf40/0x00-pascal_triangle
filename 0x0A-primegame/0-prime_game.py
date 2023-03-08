#!/usr/bin/python3
"""Maria and Ben are playing a game. Given
a set of consecutive integers starting from 1
up to and including n, they take turns choosing
a prime number from the set and removing that
number and its multiples from the set.
The player that cannot make a move loses the game
"""

cache = {'checked': 3, 'primes': {2: True, 3: True}}
res_cache = {}


def cache_primes(n):
    """ creates a cache of all primes required
    n is maximum value of all values to check for
    each round, which means if we get all the primes
    betwwen 1 and n, we won't need to calculate any
    prime again
    """
    if n <= cache['checked']:
        return

    for x in range(cache['checked'], n + 1):
        if is_prime(x):
            cache['primes'][x] = True
            cache['checked'] = n


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

    if res_cache.get(n):
        return res_cache.get(n)

    primes_count = 0
    # Since we have all prime no's we need cached
    # no need looping over n since we will be checking for the
    # prime no's already cached anyway
    # so loop over the prime no's and count how many are there
    # between 1 and n
    for prime in sorted(cache['primes'].keys()):
        if n >= prime:
            primes_count += 1
        else:
            break

    if primes_count % 2 == 0:  # Maria's turn therefore she looses
        res_cache[n] = 'b'
        return 'b'             # since if turn is even it is Maria'a
    res_cache[n] = 'm'
    return 'm'                 # else it is Ben's so Ben looses


def is_prime(n):
    """ returns true if n is prime """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    start = 3

    end = int(n ** 0.5) + 1
    while start < end:
        if n % start == 0:
            return False
        start += 2
    if n > cache['checked']:  # update checked
        cache['checked'] = n
    cache['primes'][n] = True
    return True
