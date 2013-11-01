from copy import deepcopy


class EmptyError(Exception):
    pass


class OutOfSpaceError(Exception):
    pass


class Stack:
    def __init__(self):
        self._buffer = []
        self._min_buffer = []

    def push(self, i):
        if self.is_empty() or i < self._min_buffer[-1]:
            self._min_buffer.append(i)
        else:
            self._min_buffer.append(self._min_buffer[-1])
        self._buffer.append(i)

    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        self._min_buffer.pop()
        return self._buffer.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._buffer[-1]

    def min(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._min_buffer[-1]

    def is_empty(self):
        return len(self._buffer) == 0


class FixedTripleStack:
    def __init__(self):
        #emulate array
        self._stack_size = 10
        self._buffer = []
        self._pointers = [0, 0, 0]
        for i in range(self._stack_size * 3):
            self._buffer.append(None)

    def push(self, stack_num, value):
        if self._pointers[stack_num] == self._stack_size:
            raise OutOfSpaceError('Out of space')
        index = self._stack_size * stack_num + self._pointers[stack_num]
        self._buffer[index] = value
        self._pointers[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyError('Stack is empty')
        index = self._stack_size * stack_num + self._pointers[stack_num] - 1
        value = self._buffer[index]
        self._buffer[index] = None
        self._pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyError('Stack is empty')
        index = self._stack_size * stack_num + self._pointers[stack_num] - 1
        return self._buffer[index]

    def is_empty(self, stack_num):
        return self._pointers[stack_num] == 0


class SetOfStacks:
    def __init__(self):
        self._stacks = []
        self._stack_size = 5

    def __len__(self):
        i = 0
        for stack in self._stacks:
            i += len(stack)
        return i

    def _last_stack(self) -> list:
        return self._stacks[-1]

    def push(self, value):
        if len(self) == 0 or len(self._last_stack()) == self._stack_size:
            stack = [value]
            self._stacks.append(stack)
        else:
            self._last_stack().append(value)

    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        value = self._stacks[-1].pop()
        if len(self._stacks[-1]) == 0:
            self._stacks.pop()
        return value

    def peek(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._stacks[-1][-1]

    def is_empty(self):
        return len(self) == 0


def move_disks(n: int, source: list, destination: list, buffer: list):
    if n == 0:
        return
    move_disks(n - 1, source, buffer, destination)
    destination.append(source.pop())
    move_disks(n - 1, buffer, destination, source)


def sort(stack: list) -> list:
    stack = deepcopy(stack)
    result = []
    while len(stack) > 0:
        i = stack.pop()
        while len(result) > 0 and result[-1] > i:
            stack.append(result.pop())
        result.append(i)
    return result

