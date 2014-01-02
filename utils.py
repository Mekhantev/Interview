def first(iterable):
    for item in iterable:
        return item
    raise ValueError('No satisfactory value found')


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance