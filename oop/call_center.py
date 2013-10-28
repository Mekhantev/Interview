from abc import ABCMeta
from enum import Enum
from utils import Singleton


class Rank(Enum):
    low = 0
    normal = 1
    high = 2


class Call():
    def __init__(self, rank: int):
        self.rank = rank


class Employee(metaclass=ABCMeta):
    @property
    def busy(self) -> bool:
        return self._current_call is not None

    @property
    def current_call(self) -> Call:
        return self._current_call

    def __init__(self):
        self._current_call = None
        self.rank = None

    def receive_call(self, call: Call):
        if not self.busy:
            self._current_call = call


class Operator(Employee):
    def __init__(self):
        super().__init__()
        self.rank = 0


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.rank = 1


class Director(Employee):
    def __init__(self):
        super().__init__()
        self.rank = 2


class CallHandler(metaclass=Singleton):
    @property
    def operators(self) -> tuple:
        return tuple(self._employee_levels[0])

    @property
    def managers(self) -> tuple:
        return tuple(self._employee_levels[1])

    @property
    def directors(self) -> tuple:
        return tuple(self._employee_levels[2])

    def __init__(self):
        self._employee_levels = [
            [Operator() for _ in range(5)],
            [Manager() for _ in range(2)],
            [Director() for _ in range(1)]
        ]

    def dispatch_call(self, call: Call):
        employee = self._find_not_busy_employee(call.rank)
        employee.receive_call(call)

    def _find_not_busy_employee(self, call_rank) -> Employee:
        for rank in range(call_rank, 3):
            for employee in self._employee_levels[rank]:
                if not employee.busy:
                    return employee
        raise Exception('All employees are busy')





