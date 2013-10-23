__author__ = 'Dmitry Mekhantev'


def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


def count_ways_dynamic(n, l: list):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif not l[n]:
        l[n] = (count_ways_dynamic(n - 1, l)
                + count_ways_dynamic(n - 2, l)
                + count_ways_dynamic(n - 3, l))
    return l[n]