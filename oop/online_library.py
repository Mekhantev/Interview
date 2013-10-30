class Book():
    def __init__(self, author, title, body):
        self.author = author
        self.title = title
        self.body = body


class User():
    @property
    def login(self):
        return self._login

    def __init__(self, login):
        self._login = login
        self.current_book = None


class UserAlreadyExistsError(Exception):
    pass


class IncorrectAuthDataError(Exception):
    pass


class UserNotLoggedInError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class OnlineLibrary():
    def __init__(self):
        self._books = {}
        self._add_book('Ray Bradbury', 'Fahrenheit 451', 'aaa')
        self._add_book('George Orwell', '1984', 'bbb')
        self._add_book('Aldous Huxley', 'Brave New World', 'ccc')
        self._users = {}
        self._active_users = []

    def register(self, login, password):
        key = self._get_key(login, password)
        user = self._users.get(key, None)
        if user:
            raise UserAlreadyExistsError('User with this login already exists')
        self._users[key] = User(login)

    def login(self, login_, password) -> User:
        user = self._users.get(self._get_key(login_, password), None)
        if user is None:
            raise IncorrectAuthDataError('Wrong auth data')
        self._active_users.append(user)
        return user

    def logout(self, user: User):
        self._active_users.remove(user)

    def get_book(self, user: User, author: str, title: str):
        if not user in self._active_users:
            raise UserNotLoggedInError('Login first')
        book = self._books.get(self._get_key(author, title), None)
        if book is None:
            raise BookNotFoundError('Book not found')
        user.current_book = book

    def _get_key(self, primary: str, secondary: str):
        return hash(primary + ' ' + secondary)

    def _add_book(self, author, title, body):
        book = Book(author, title, body)
        key = self._get_key(author, title)
        self._books[key] = book