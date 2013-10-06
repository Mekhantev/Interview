__author__ = 'Dmitry Mekhantev'


class Stack:
    buffer = []
    min_buffer = []

    def push(self, i):
        if self.is_empty() or i < self.min_buffer[-1]:
            self.min_buffer.append(i)
        else:
            self.min_buffer.append(self.min_buffer[-1])
        self.buffer.append(i)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        self.min_buffer.pop()
        return self.buffer.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.buffer[-1]

    def min(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.min_buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0


class FixedTripleStack:
    stack_size = 10
    buffer = []
    pointers = [0, 0, 0]

    def __init__(self):
        #emulate array
        for i in range(0, self.stack_size * 3):
            self.buffer.append(None)

    def push(self, stack_num, value):
        index = self.stack_size * stack_num + self.pointers[stack_num] + 1
        if self.pointers[stack_num] + 1 == self.stack_size:
            raise Exception('Out of space')
        self.buffer[index] = value
        self.pointers[stack_num] += 1

    def pop(self, stack_num):
        if self.pointers[stack_num] == 0:
            raise Exception('Stack is empty')
        index = self.stack_size * stack_num + self.pointers[stack_num]
        value = self.buffer[index]
        self.buffer[index] = None
        self.pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.pointers[stack_num] == 0:
            raise Exception('Stack is empty')
        index = self.stack_size * stack_num + self.pointers[stack_num]
        return self.buffer[index]

    def is_empty(self, stack_num):
        return self.pointers[stack_num] == 0