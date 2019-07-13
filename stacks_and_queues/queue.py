class Node:
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self, value):
        self.start = Node(value)
        self.end = self.start

    def add(self, value):
        new_last = Node(value)
        self.end.next = new_last
        self.end = new_last

    def remove(self):
        first = self.start
        if self.start:
            self.start = self.start.next
        return first

    def peek(self):
        return self.start

    def is_empty(self):
        return self.start is None

    def __str__(self):
        aux = self.start
        values = []
        while aux:
            values.append(str(aux.value))
            aux = aux.next
        return ','.join(values)


# Tests:
queue = Queue(1)
queue.add(2)
queue.add(3)
queue.add(4)
print(queue)
print(queue.peek())
print(queue.is_empty())
queue.remove()
print(queue)
queue.remove()
print(queue)
queue.remove()
print(queue)
queue.remove()
print(queue)
print(queue.remove())
print(queue.is_empty())
