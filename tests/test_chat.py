from unittest import TestCase
from structures.chat import Server


class TestServer(TestCase):
    def test_register(self):
        server = Server()
        login = 'Dmitry'
        password = 'abcdef'
        server.register(login, password)
        client = server.login(login, password)
        self.assertEqual(login, client.login)
        self.assertRaises(Exception, server.register, login, password)

    def test_login(self):
        server = Server()
        login = 'Dmitry'
        password = 'abcdef'
        server.register(login, password)
        client = server.login(login, password)
        self.assertEqual(login, client.login)
        self.assertRaises(Exception, server.login, 'a', 'b')
        self.assertRaises(Exception, server.login, login, 'b')
        self.assertRaises(Exception, server.login, login, password)

    def test_logout(self):
        server = Server()
        login = 'Dmitry'
        password = 'abcdef'
        server.register(login, password)
        client = server.login(login, password)
        self.assertEqual(login, client.login)
        server.logout(client)
        self.assertEqual(0, len(server._active_clients))

    def test_send_message(self):
        server = Server()
        login = 'Dmitry'
        password = 'abcdef'
        server.register(login, password)
        client = server.login(login, password)
        self.assertEqual(login, client.login)
        server.logout(client)
        message = 'Hello!'
        recipient = 'Alien'
        self.assertRaises(Exception, server.send_message, message, client, recipient)
        client2 = server.login(login, password)
        self.assertRaises(Exception, server.send_message, message, client, recipient)
        client = client2
        self.assertRaises(Exception, server.send_message, message, client, "abcd")
        r_password = 'abc'
        server.register(recipient, r_password)
        client2 = server.login(recipient, r_password)
        server.send_message(message, client, client2.login)
        self.assertEqual(client2.inbox[0].text, message)

