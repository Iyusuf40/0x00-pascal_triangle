#!/usr/bin/python3
""" contains function that computes the least number of change
required to make"""


def makeChange(coins, total):
    if total < 1:
        return 0
    coins = sorted(coins, reverse=True)
    for index in range(len(coins)):
        res = check_from_next_index(coins, total, index)
        if res != -1:
            return res
    return -1


def check_from_next_index(coins, total, index):
    coins = coins[index:]
    num = 0
    tot = 0
    for coin in coins:
        if total >= coin:
            div = total // coin
            rem = total - (coin * div)
            num += div
            total = rem
            if total == 0:
                return num
    return -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
