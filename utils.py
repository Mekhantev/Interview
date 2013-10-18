__author__ = 'Dmitry Mekhantev'


def first(iterable):
    for item in iterable:
        return item
    raise ValueError('No satisfactory value found')