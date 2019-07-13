from stacks_and_queues.stack import Stack
import copy


# Time/Space O(n)
def find_min_max(stack, pos):
    aux = copy.copy(stack)  # copy over here
    i, min, max = 0, None, None
    size = aux.size
    while i < size - pos:
        value = aux.pop()
        if i >= pos:
            if max is None or value > max:
                max = value
            if min is None or value < min:
                min = value
        i += 1
    return min, max


def sort_stack(stack):
    i, j = 0, int(stack.size/2)
    size = stack.size
    while i < j:
        min, max = find_min_max(stack, i)
        k = 0
        aux = Stack()
        while k <= size:
            if k == size - i:
                aux.push(max)
            else:
                value = stack.pop()
                if value != max:
                    aux.push(value)
            k += 1
        k = 0
        stack = Stack()
        while k <= size:
            if k == size - i:
                stack.push(min)
            else:
                value = aux.pop()
                if value != min:
                    stack.push(value)
            k += 1
        i += 1
    return stack


# Space O(n). Time O(n^2)
def sort_stack2(stack):
    changes = 0
    is_max = True
    while changes < stack.size - 1 or not is_max:
        aux = Stack()
        changes = 0
        max_min = stack.pop()
        while not stack.is_empty():
            v = stack.pop()
            if (is_max and v > max_min) or (not is_max and v < max_min):
                max_min, v = v, max_min
                changes += 1
            aux.push(v)
        aux.push(max_min)
        stack = aux
        is_max = not is_max
    return stack


# Tests:
# stack = Stack()
# stack.push(3)
# stack.push(2)
# stack.push(4)
# stack.push(1)
# stack.push(6)
# stack.push(5)
# print(stack)
# print(sort_stack2(stack))
