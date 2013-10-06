__author__ = 'Dmitry Mekhantev'


class Stack:
    def __init__(self):
        self.buffer = []
        self.min_buffer = []

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
    def __init__(self):
        #emulate array
        self.stack_size = 10
        self.buffer = []
        self.pointers = [0, 0, 0]
        for i in range(0, self.stack_size * 3):
            self.buffer.append(None)

    def push(self, stack_num, value):
        if self.pointers[stack_num] == self.stack_size:
            raise Exception('Out of space')
        index = self.stack_size * stack_num + self.pointers[stack_num]
        self.buffer[index] = value
        self.pointers[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        index = self.stack_size * stack_num + self.pointers[stack_num] - 1
        value = self.buffer[index]
        self.buffer[index] = None
        self.pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        index = self.stack_size * stack_num + self.pointers[stack_num] - 1
        return self.buffer[index]

    def is_empty(self, stack_num):
        return self.pointers[stack_num] == 0