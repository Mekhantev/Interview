class Pair():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class OutOfSpaceError(Exception):
    pass


class ItemAlreadyExistsError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


class HashTable():
    @property
    def _max_items(self):
        return 10  # fixed size

    def __init__(self):
        self._items = [None for _ in range(self._max_items)]
        self._current_items_number = 0

    def add(self, pair: Pair):
        if self._current_items_number == self._max_items:
            raise OutOfSpaceError('Hash table has no empty space')
        i = self._hash(pair.key)
        if not self._items[i]:
            self._items[i] = [pair]
        else:
            for e in self._items[i]:
                if e.key == pair.key:
                    raise ItemAlreadyExistsError('Item with the same key already exists')
            self._items[i].append(pair)
        self._current_items_number += 1

    def get(self, key):
        i = self._hash(key)
        if not self._items[i]:
            raise ItemNotFoundError('There is no element with such key')
        for e in self._items[i]:
            if e.key == key:
                return e
        raise ItemNotFoundError('There is no element with such key')

    def _hash(self, key) -> int:
        h = 0
        for c in str(key):
            h = 101 * h + ord(c)
        return h % len(self._items)