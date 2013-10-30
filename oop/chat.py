from datetime import datetime
from uuid import uuid1


class Client():
    @property
    def id(self):
        return self._id

    @property
    def login(self):
        return self._login

    def __init__(self, id_, login):
        self._id = id_
        self._login = login
        self.inbox = []


class User():
    @property
    def login(self):
        return self._login

    @property
    def hashed_password(self):
        return self._hashed_password

    def __init__(self, login, password):
        self._login = login
        self._hashed_password = hash(password)


class Message():
    def __init__(self, text, date, from_, to):
        self.text = text
        self.date = date
        self.from_ = from_
        self.to = to


class UserAlreadyExistsError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class IncorrectAuthDataError(Exception):
    pass


class UserLoggedInError(Exception):
    pass


class UserNotLoggedInError(Exception):
    pass


class Server():
    def __init__(self):
        self._users = {}
        self._active_clients = {}
        self._history = []

    def register(self, login, password):
        user = self._users.get(login)
        if user:
            raise UserAlreadyExistsError('User with this login already exists')
        self._users[login] = User(login, password)

    def login(self, login_, password) -> Client:
        user = self._users.get(login_)
        if not user:
            raise UserNotFoundError('User doesnt exist')
        if user.hashed_password != hash(password):
            raise IncorrectAuthDataError('Wrong auth data')
        if self._active_clients.get(user.login):
            raise UserLoggedInError('User has already logged in')
        id_ = uuid1()
        client = Client(id_, user.login)
        self._active_clients[user.login] = client
        return client

    def logout(self, client: Client):
        del self._active_clients[client.login]

    def send_message(self, message: str, client: Client, recipient: str):
        c = self._active_clients.get(client.login)
        if not c:
            raise UserNotLoggedInError('Login first')
        if c.id != client.id:
            raise UserLoggedInError('User logged in from another client')
        r = self._users.get(recipient)
        if not r:
            raise UserNotFoundError('Recipient doesnt exist')
        m = Message(message, datetime.utcnow(), c.login, r.login)
        r_c = self._active_clients.get(recipient)
        if r_c:
            r_c.inbox.append(m)
        self._history.append(m)