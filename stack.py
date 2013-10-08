from copy import deepcopy

__author__ = 'Dmitry Mekhantev'


class Stack:
    def __init__(self):
        self.__buffer = []
        self.__min_buffer = []

    def push(self, i):
        if self.is_empty() or i < self.__min_buffer[-1]:
            self.__min_buffer.append(i)
        else:
            self.__min_buffer.append(self.__min_buffer[-1])
        self.__buffer.append(i)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        self.__min_buffer.pop()
        return self.__buffer.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.__buffer[-1]

    def min(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.__min_buffer[-1]

    def is_empty(self):
        return len(self.__buffer) == 0


class FixedTripleStack:
    def __init__(self):
        #emulate array
        self.__stack_size = 10
        self.__buffer = []
        self.__pointers = [0, 0, 0]
        for i in range(0, self.__stack_size * 3):
            self.__buffer.append(None)

    def push(self, stack_num, value):
        if self.__pointers[stack_num] == self.__stack_size:
            raise Exception('Out of space')
        index = self.__stack_size * stack_num + self.__pointers[stack_num]
        self.__buffer[index] = value
        self.__pointers[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        index = self.__stack_size * stack_num + self.__pointers[stack_num] - 1
        value = self.__buffer[index]
        self.__buffer[index] = None
        self.__pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        index = self.__stack_size * stack_num + self.__pointers[stack_num] - 1
        return self.__buffer[index]

    def is_empty(self, stack_num):
        return self.__pointers[stack_num] == 0


class SetOfStacks:
    def __init__(self):
        self.__stacks = []
        self.__stack_size = 5

    def __len__(self):
        i = 0
        for stack in self.__stacks:
            i += len(stack)
        return i

    def __last_stack(self) -> list:
        return self.__stacks[-1]

    def push(self, value):
        if len(self) == 0 or len(self.__last_stack()) == self.__stack_size:
            stack = [value]
            self.__stacks.append(stack)
        else:
            self.__last_stack().append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        value = self.__stacks[-1].pop()
        if len(self.__stacks[-1]) == 0:
            self.__stacks.pop()
        return value

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.__stacks[-1][-1]

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

