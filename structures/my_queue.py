from abc import ABCMeta
from structures.linked_list import Node


class StacksBasedQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            raise Exception('Queue is empty')
        return self.stack2.pop()


class Animal(metaclass=ABCMeta):
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        #linked list as data storage
        self._first_animal = None
        self._last_animal = None

    def enqueue(self, animal: Animal):
        if not self._first_animal:
            self._first_animal = Node(animal)
        elif not self._last_animal:
            self._last_animal = Node(animal)
            self._first_animal.next = self._last_animal
        else:
            self._last_animal.next = Node(animal)
            self._last_animal = self._last_animal.next

    def dequeue(self) -> Animal:
        if not self._first_animal:
            raise Exception('Queue is empty')
        animal = self._first_animal.data
        self._first_animal = self._first_animal.next
        if not self._first_animal:
            self._last_animal = None
        return animal

    def _dequeue_by_type(self, animal_type):
        if not self._first_animal:
            raise Exception('Queue is empty')
        current = self._first_animal
        if isinstance(current.data, animal_type):
            self._first_animal = current.next
            return current.data
        previous = current
        while current is not None:
            if isinstance(current.data, animal_type):
                previous.next = current.next
                return current.data
            previous = current
            current = current.next
        return None

    def dequeue_cat(self) -> Cat:
        cat = self._dequeue_by_type(Cat)
        if not cat:
            raise Exception('No cats in queue')
        return cat

    def dequeue_dog(self) -> Dog:
        dog = self._dequeue_by_type(Dog)
        if not dog:
            raise Exception('No dogs in queue')
        return dog
