from unittest import TestCase
from oop.social_network import *


class TestPerson(TestCase):
    def test_add_friend(self):
        p1 = Person(1, 'Dmitry')
        p2 = Person(2, 'Alex')
        p3 = Person(3, 'Michael')
        p3.add_friend(p1.id)
        p3.add_friend(p2.id)
        self.assertEqual(2, len(p3._friends))


class TestServer(TestCase):
    def test_add_machine(self):
        server = Server()
        server.add_machine()
        server.add_machine()
        self.assertEqual(5, len(server._machines))

    def test_add_person(self):
        server = Server()
        server.add_person('Dmitry')
        server.add_person('Alex')
        server.add_person('Michael')
        self.assertEqual(3, server.count_users())

    def test_get_person(self):
        server = Server()
        p1 = server.add_person('Dmitry')
        p2 = server.add_person('Alex')
        p3 = server.add_person('Michael')
        self.assertEqual(p1, server.get_person(p1.id))
        self.assertEqual(p2, server.get_person(p2.id))
        self.assertEqual(p3, server.get_person(p3.id))