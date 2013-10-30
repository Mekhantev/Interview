from unittest import TestCase
from oop.online_library import *


class TestOnlineLibrary(TestCase):
    def test_register(self):
        ol = OnlineLibrary()
        login = 'Dmitry'
        password = 'abcdef'
        ol.register(login, password)
        user = ol.login(login, password)
        self.assertEqual(login, user.login)
        self.assertRaises(UserAlreadyExistsError, ol.register, login, password)

    def test_login(self):
        ol = OnlineLibrary()
        login = 'Dmitry'
        password = 'abcdef'
        ol.register(login, password)
        user = ol.login(login, password)
        self.assertEqual(login, user.login)
        self.assertRaises(IncorrectAuthDataError, ol.login, 'a', 'b')

    def test_logout(self):
        ol = OnlineLibrary()
        login = 'Dmitry'
        password = 'abcdef'
        ol.register(login, password)
        user = ol.login(login, password)
        self.assertEqual(login, user.login)
        ol.logout(user)
        self.assertEqual(0, len(ol._active_users))

    def test_get_book(self):
        ol = OnlineLibrary()
        login = 'Dmitry'
        password = 'abcdef'
        ol.register(login, password)
        user = ol.login(login, password)
        self.assertEqual(login, user.login)
        author = 'George Orwell'
        title = '1984'
        ol.get_book(user, author, title)
        self.assertEqual(user.current_book.author, author)
        self.assertEqual(user.current_book.title, title)
        ol.logout(user)
        self.assertRaises(UserNotLoggedInError, ol.get_book, user, author, title)
        user = ol.login(login, password)
        self.assertRaises(BookNotFoundError, ol.get_book, user, 'a', title)