from unittest import TestCase
from oop.social_network import *


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
        self.fail()
        #server = Server()
        #server.add_person('Dmitry')
        #server.add_person('Alex')
        #p1 = server.add_person('Michael')
        #print(p1._id)
        #p2 = server.get_person(p1.id)
        #self.assertEqual(p1, p2)