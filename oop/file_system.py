from abc import ABCMeta, abstractproperty
import os
from utils import datetime_now_float

__author__ = 'Dmitry Mekhantev'


class Entry(metaclass=ABCMeta):
    @property
    def full_path(self) -> str:
        return (os.path.join(self.parent.full_path, self.name)
                if self.parent
                else self.name)

    @abstractproperty
    def size(self):
        """ Get entry size """

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.creation_date = datetime_now_float()
        self.modification_date = self.creation_date


class Directory(Entry):
    @property
    def size(self):
        return sum(e.size for e in self._entries)

    @property
    def entries(self):
        return tuple(self._entries)

    def __init__(self, name: str, parent=None):
        super().__init__(name, parent)
        self._entries = []

    def count_entries(self) -> int:
        count = 0
        for e in self._entries:
            if isinstance(e, Directory):
                count += e.count_entries()
            count += 1
        return count

    def add_entry(self, entry: Entry):
        if entry in self._entries:
            raise Exception('Item already exists in this directory')
        if any(e for e in self._entries if e.name == entry.name):
            raise Exception('Item with the same name already exists')
        self._entries.append(entry)

    def remove_entry(self, entry: Entry):
        if not entry in self._entries:
            return
        self._entries.remove(entry)


class File(Entry):
    @property
    def size(self):
        return len(self.content)

    def __init__(self, name: str, content: str, parent: Directory):
        super().__init__(name, parent)
        self.content = content