from collections.abc import Iterable
from enum import Enum


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


class Field():
    def __init__(self, i=5, nonfree_points: Iterable=None):
        self._matrix = []
        self._nonfree_points = []
        self._nonfree_points.extend(nonfree_points)
        for _ in range(i):
            self._matrix.append([None for _ in range(i)])

    def get_path(self, t: tuple, path: list, cache: dict):
        path.append(t)
        #b = cache.get(t)
        #if b is not None:
        #    return b
        x = t[0]
        y = t[1]
        if x == 0 and y == 0:
            return True
        next_p = (x - 1, y)
        b = False
        if x > 0 and self._is_free(next_p):
            b = self.get_path(next_p, path, cache)
        next_p = (x, y - 1)
        if not b and y > 0 and self._is_free(next_p):
            b = self.get_path(next_p, path, cache)
            #if not b:
        #    path.remove(t)
        cache[t] = b
        return b

    def _is_free(self, t: tuple):
        if t in self._nonfree_points:
            return False
        return True


def find_magic_index(ints: 'Sorted linear collection',
                     left: int, right: int) -> int:
    """Returns index if ints[index] == index"""
    pos = (left + right) // 2
    if ints[pos] == pos:
        return pos
    elif ints[pos] < pos:
        return find_magic_index(ints, pos + 1, right)
    else:
        return find_magic_index(ints, left, pos - 1)


def generate_brackets(n):
    for i in range(1, n + 1):
        yield from _generate_brackets('', 0, 0, i)


def _generate_brackets(s, op, cl, pairs):
    if op == pairs and cl == pairs:
        yield s
    else:
        if op < pairs:
            yield from _generate_brackets(s + '(', op + 1, cl, pairs)
        if cl < op:
            yield from _generate_brackets(s + ')', op, cl + 1, pairs)


class Color(Enum):
    black = 1
    red = 2
    blue = 3


def flood_fill(screen: list, x, y, old_color: Color, new_color: Color):
    if x < 0 or x == len(screen[0]) or y < 0 or y == len(screen):
        return
    if screen[y][x] != old_color:
        return
    screen[y][x] = new_color
    flood_fill(screen, x - 1, y, old_color, new_color)
    flood_fill(screen, x + 1, y, old_color, new_color)
    flood_fill(screen, x, y + 1, old_color, new_color)
    flood_fill(screen, x, y - 1, old_color, new_color)


def make_change(n, denom):
    next_denom = 0
    if denom == 25:
        next_denom = 10
    elif denom == 10:
        next_denom = 5
    elif denom == 5:
        next_denom = 1
    else:
        return 1
    ways = 0
    i = 0
    while i * denom <= n:
        ways += make_change(n - i * denom, next_denom)
        i += 1
    return ways
