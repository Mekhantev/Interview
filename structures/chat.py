from datetime import datetime
from uuid import uuid1

__author__ = 'Dmitry Mekhantev'


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


class Server():
    def __init__(self):
        self._users = {}
        self._active_clients = {}
        self._history = []

    def register(self, login, password):
        user = self._users.get(login)
        if user:
            raise Exception('User with this login already exists')
        self._users[login] = User(login, password)

    def login(self, login_, password) -> Client:
        user = self._users.get(login_)
        if not user:
            raise Exception('User doesnt exist')
        if user.hashed_password != hash(password):
            raise Exception('Wrong auth data')
        if self._active_clients.get(user.login):
            raise Exception('User has already logged in')
        id_ = uuid1()
        client = Client(id_, user.login)
        self._active_clients[user.login] = client
        return client

    def logout(self, client: Client):
        del self._active_clients[client.login]

    def send_message(self, message: str, client: Client, recipient: str):
        c = self._active_clients.get(client.login)
        if not c:
            raise Exception('Login first')
        if c.id != client.id:
            raise Exception('User logged in from another client')
        r = self._users.get(recipient)
        if not r:
            raise Exception('Recipient doesnt exist')
        m = Message(message, datetime.utcnow(), c.login, r.login)
        r_c = self._active_clients.get(recipient)
        if r_c:
            r_c.inbox.append(m)
        self._history.append(m)



