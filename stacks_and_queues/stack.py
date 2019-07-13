class Node:
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Stack:
    size = 0
    top = None

    def __init__(self, value=None):
        if value is not None:
            self.top = Node(value)
            self.size += 1

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top
        self.size += 1

    def pop(self):
        cur_top = self.top
        self.size -= 1
        if self.top:
            self.top = self.top.next
        if cur_top:
            return cur_top.value

    def peek(self):
        if self.top:
            return self.top.value

    def is_empty(self):
        return self.top is None

    def __str__(self):
        aux = self.top
        values = []
        while aux:
            values.append(str(aux.value))
            aux = aux.next
        return ','.join(values)


# Tests:
# stack = Stack(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack)
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
