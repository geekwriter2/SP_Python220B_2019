# Stella Kim
# Activity 2: Logging and Debugging

"""Logging Activity"""

import sys


def my_fun(n):
    if n < 1:
        return False
    if n == 2:
        return True
    return my_fun(n / 2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(my_fun(n))