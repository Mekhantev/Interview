__author__ = 'Dmitry Mekhantev'


def _identity(item):
    return item


def first(iterable, predicate=_identity):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError('No satisfactory value found')