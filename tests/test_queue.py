from unittest import TestCase
from structures.my_queue import *


class TestAnimalQueue(TestCase):
    def test_enqueue(self):
        queue = AnimalQueue()
        animals = [Cat(), Dog(), Dog(), Cat(), Cat()]
        for animal in animals:
            queue.enqueue(animal)
        for animal in animals:
            self.assertEqual(animal, queue.dequeue())

    def test_dequeue(self):
        queue = AnimalQueue()
        animals = [Cat(), Dog(), Dog(), Cat(), Cat()]
        for animal in animals:
            queue.enqueue(animal)
        for animal in animals:
            self.assertEqual(animal, queue.dequeue())
        self.assertRaises(Exception, queue.dequeue)

    def test_dequeue_cat(self):
        queue = AnimalQueue()
        animals = [Cat(), Dog(), Dog(), Cat(), Cat()]
        for animal in animals:
            queue.enqueue(animal)
        cats = (animal for animal in animals if isinstance(animal, Cat))
        for cat in cats:
            self.assertEqual(cat, queue.dequeue_cat())
        self.assertRaises(Exception, queue.dequeue_cat)
        queue = AnimalQueue()
        cats = [Cat(), Cat()]
        for cat in cats:
            queue.enqueue(cat)
        for cat in cats:
            self.assertEqual(cat, queue.dequeue_cat())
        self.assertRaises(Exception, queue.dequeue_cat)

    def test_dequeue_dog(self):
        queue = AnimalQueue()
        animals = [Cat(), Dog(), Dog(), Cat(), Cat()]
        for animal in animals:
            queue.enqueue(animal)
        dogs = (animal for animal in animals if isinstance(animal, Dog))
        for dog in dogs:
            self.assertEqual(dog, queue.dequeue_dog())
        self.assertRaises(Exception, queue.dequeue_dog)
        queue = AnimalQueue()
        dogs = [Dog(), Dog()]
        for dog in dogs:
            queue.enqueue(dog)
        for dog in dogs:
            self.assertEqual(dog, queue.dequeue_dog())
        self.assertRaises(Exception, queue.dequeue_dog)


class TestStacksBasedQueue(TestCase):
    def test_enqueue(self):
        queue = StacksBasedQueue()
        values = (1, 3, 2, 7, 8, 5, 9)
        for i in values:
            queue.enqueue(i)
        for i in values:
            self.assertEqual(queue.dequeue(), i)

    def test_dequeue(self):
        queue = StacksBasedQueue()
        values = (1, 3, 2, 7, 8, 5, 9)
        for i in values:
            queue.enqueue(i)
        for i in values[:-2]:
            self.assertEqual(queue.dequeue(), i)
        new_values = (10, 5)
        values = values[-2:] + new_values
        for i in new_values:
            queue.enqueue(i)
        for i in values:
            self.assertEqual(queue.dequeue(), i)
        self.assertRaises(Exception, queue.dequeue)