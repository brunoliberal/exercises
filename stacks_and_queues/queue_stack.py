import copy

from stacks_and_queues.stack import Stack


class QueueStack:
    def __init__(self, value):
        self.stack = Stack(value)
        self.r_stack = Stack(value)

    def add(self, value):
        self.stack.push(value)
        self.flip_stack()

    def remove(self):
        value = self.r_stack.pop()
        self.unflip_stack()
        return value

    def peek(self):
        return self.r_stack.peek()

    def is_empty(self):
        return self.r_stack.is_empty()

    def __str__(self):
        return str(self.stack) + '  -  ' + str(self.r_stack)

    def flip_stack(self):
        aux = copy.copy(self.stack)  # or use a array to pop the two stacks
        self.r_stack = Stack(aux.pop())
        while not aux.is_empty():
            self.r_stack.push(aux.pop())

    def unflip_stack(self):
        aux = copy.copy(self.r_stack)
        self.stack = Stack(aux.pop())
        while not aux.is_empty():
            self.stack.push(aux.pop())


# Tests:
# stack = QueueStack(1)
# stack.add(2)
# stack.add(3)
# stack.add(4)
# stack.add(5)
# print(stack)
# print(stack.peek())
# print(stack.is_empty())
# print(stack.remove())
# print(stack.remove())
# print(stack.remove())
# print(stack.remove())
# print(stack.remove())
# print(stack.remove())
# print(stack.is_empty())
