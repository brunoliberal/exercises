class ArrayStack:
    MAX_ELEMENTS = 10
    stacks = [None] * MAX_ELEMENTS

    def __init__(self, value):
        self.stacks[0] = value
        self.top_idx = 0
        self.real_size = 1

    def push(self, value):
        self.real_size += 1
        if self.real_size > self.MAX_ELEMENTS:
            self.grow_array()
        self.top_idx += 1
        self.stacks[self.top_idx] = value

    def grow_array(self):
        self.MAX_ELEMENTS = self.MAX_ELEMENTS * 2
        self.stacks.extend([None] * self.MAX_ELEMENTS)

    def pop(self):
        if self.real_size > 0:
            value, self.stacks[self.top_idx] = self.stacks[self.top_idx], None
            self.top_idx -= 1
            self.real_size -= 1
            return value

    def peek(self):
        return self.stacks[self.top_idx]

    def is_empty(self):
        return self.real_size == 0

    def __str__(self):
        return str(self.stacks)


# Tests:
# stack = ArrayStack(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
# stack.push(4)
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
