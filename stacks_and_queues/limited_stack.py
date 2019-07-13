MAX_ELEMENTS = 5


class LimitedStack:
    MAX_STACKS = 3
    stacks = [[None] * MAX_ELEMENTS for i in range(MAX_STACKS)]

    def __init__(self, value):
        self.stacks[0][0] = value
        self.cur_stack_top_idx = 0
        self.cur_stack_size = 1
        self.cur_stack_idx = 0

    def push(self, value):
        if self.cur_stack_size >= MAX_ELEMENTS:
            if self.cur_stack_idx >= self.MAX_STACKS - 1:
                self.increase_stacks_pile()
            self.change_stack()
        self.cur_stack_top_idx += 1
        self.cur_stack_size += 1
        self.stacks[self.cur_stack_idx][self.cur_stack_top_idx] = value

    def increase_stacks_pile(self):
        self.MAX_STACKS = self.MAX_STACKS * 2
        self.stacks.extend([[None] * MAX_ELEMENTS for i in range(self.MAX_STACKS)])

    def change_stack(self):
        self.cur_stack_idx += 1
        self.cur_stack_top_idx = -1
        self.cur_stack_size = 0

    def pop(self):
        if not self.is_empty():
            value, self.stacks[self.cur_stack_idx][self.cur_stack_top_idx] = self.stacks[self.cur_stack_idx][self.cur_stack_top_idx], None
            self.cur_stack_top_idx -= 1
            self.cur_stack_size -= 1
            if self.cur_stack_top_idx < 0 < self.cur_stack_idx:
                self.cur_stack_idx -= 1
                self.cur_stack_size = MAX_ELEMENTS
                self.cur_stack_top_idx = MAX_ELEMENTS - 1
            return value

    def peek(self):
        if not self.is_empty():
            return self.stacks[self.cur_stack_idx][self.cur_stack_top_idx]

    def is_empty(self):
        return self.cur_stack_size == 0

    def __str__(self):
        return str(self.stacks)


# Tests:
# stack = LimitedStack(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# stack.push(9)
# stack.push(10)
# stack.push(11)
# stack.push(12)
# stack.push(13)
# stack.push(14)
# stack.push(15)
# print(stack)
# stack.push(16)
# print(stack)
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
