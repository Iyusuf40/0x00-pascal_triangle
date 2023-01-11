#!/usr/bin/python3
""" module doc string """


def minOperations(n):
    """min ops"""

    if not isinstance(n, int):
        return 0

    if not n or (isinstance(n, int) and n < 0):
        return 0

    if n <= 1:
        return 0

    all_max_divs = set()

    divisors = get_divisors(n)

    path = sorted(get_halves_recurs(divisors, all_max_divs))

    res = get_ops(path, n)
    return res  # if res <= n else 0


def get_divisors(n: int):
    """ returns divisors of n """
    lst = [1]
    if n % 2 == 0:
        lst.append(n / 2)
        return lst
    x = 3
    half = n / 2
    while x <= half:
        if n % x == 0:
            lst.append(n / x)
            return lst
        x = x + 2

    return lst


# def get_divisors(n: int):
#     """ returns divisors of n """
#     lst = []
#     half = n / 2
#     x = 1  # if n % 2 else 2
#     while x < half + 1:
#         if n % x == 0:
#             lst.append(x)
#         x = x + 1

#     return lst


def get_halves_recurs(lst, all_max_divs):
    """ recursively get the max divisors of each max divisor """
    max = lst[-1]
    all_max_divs.add(max)
    divisors = get_divisors(max)
    if max == 1:
        return all_max_divs
    return get_halves_recurs(divisors, all_max_divs)


def get_ops(lst, n):
    """ computes number of operatons needed"""
    lst.append(n)
    ln = len(lst)
    idx = 0
    res = 0

    # print(lst)
    while idx < ln - 1:
        res = res + (lst[idx + 1] / lst[idx])
        idx = idx + 1

    return int(res)


if __name__ == "__main__":
    import time
    # start = time.perf_counter()
    # for x in range(200):
    #     print(minOperations(x), f"for {x}")
    # print(time.perf_counter() - start)
    print(minOperations(1000), "for 1000")
    print(minOperations(-1), "for negative no")
    print(minOperations(1), "for 1")
    print(minOperations(2), "for 2")
    # print(minOperations("hello"), "for not int")
    print(minOperations(3), "for 3")
    print(minOperations(8), "for 8")
    print(minOperations(17), "for 17")
    print(minOperations(50), "for 50")
    print(minOperations(9), "for 9")
    print(minOperations(4), "for 4")
    print(minOperations(12), "for 12")
