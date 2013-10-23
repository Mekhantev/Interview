__author__ = 'Dmitry Mekhantev'


def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)
