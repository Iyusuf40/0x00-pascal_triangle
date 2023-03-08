#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}\n".format(isWinner(5, [2, 5, 1, 4, 3])))
assert isWinner(5, [2, 5, 1, 4, 3]) == 'Ben'
print("Winner: {}\n".format(isWinner(3, [4, 5, 1])))
assert isWinner(3, [4, 5, 1]) == 'Ben'
print("Winner: {}\n".format(isWinner(6, [21, 5, 1, 2, 49, 2])))
assert isWinner(6, [21, 5, 1, 2, 49, 2]) == 'Maria'
print("Winner: {}\n".format(isWinner(7, [9, 2, 13, 3, 1, 1, 2])))
assert isWinner(7, [9, 2, 13, 3, 1, 1, 2]) == 'Ben'
print("Winner: {}\n".format(isWinner(2, [2, 3])))
assert isWinner(2, [2, 3]) == None

