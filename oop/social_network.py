from collections.abc import Iterable


class Person():
    @property
    def id(self):
        return self._id

    def __init__(self, id_: int, name, friends: Iterable=None):
        self._id = id_
        self._friends = []
        self.name = name
        if friends:
            self._friends.extend(friends)

    def add_friend(self, id_: int):
        self._friends.append(id_)


class Machine():
    @property
    def id(self):
        return self._id

    def __init__(self, id_: int, persons: Iterable=None):
        self._id = id_
        self._persons = {}
        if not persons:
            return
        for person in persons:
            self.add_person(person)

    def add_person(self, person: Person):
        self._persons[person.id] = person

    def get_person(self, id_: int) -> Person:
        return self._persons[id_]

    def get_persons_number(self):
        return len(self._persons)


class Server():
    def __init__(self, machines_number: int=3):
        self._person_id = 1
        self._machine_id = 1
        self._machines = {}
        self._person_to_machine = {}
        for _ in range(machines_number):
            self.add_machine()

    def get_person(self, id_: int) -> Person:
        machine_id = self._person_to_machine[id_]
        machine = self._machines[machine_id]
        return machine.get_person(id_)

    def add_machine(self):
        machine_id = self._machine_id
        self._machines[machine_id] = Machine(machine_id)
        self._machine_id += 1

    def add_person(self, name, friends=None) -> Person:
        person_id = self._person_id
        person = Person(person_id, name, friends)
        machine = self._get_machine_with_min_persons()
        machine.add_person(person)
        self._person_to_machine[person_id] = machine.id
        self._person_id += 1
        return Person

    def count_users(self):
        return sum(kv[1].get_persons_number() for kv in self._machines.items())

    def _get_machine_with_min_persons(self):
        return min(self._machines.items(), key=lambda kv: kv[1].get_persons_number())[1]