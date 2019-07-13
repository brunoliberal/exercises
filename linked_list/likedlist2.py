class Node:
    next = None

    def __init__(self, value):
        self.value = value


class LinkedList:
    head = None

    def __init__(self, value=None):
        if value:
            self.head = Node(value)

    def add(self, value):
        aux = self.head
        if not aux:
            self.head = Node(value)
            return
        while aux.next:
            aux = aux.next
        aux.next = Node(value)

    def remove(self, value=None):
        aux = self.head
        if not aux:
            return

        if not value or aux.value == value:
            v = self.head.value
            self.head = aux.next
            return v

        while aux.next:
            if aux.next.value == value:
                v = aux.next.value
                aux.next = aux.next.next
                return v
            aux = aux.next

    def __str__(self):
        aux = self.head
        values = []
        while aux:
            values.append(str(aux.value))
            aux = aux.next
        return ','.join(values)


# Tests:
# ll = LinkedList(5)
# print(ll)
# ll.add(4)
# print(ll)
# ll.add(3)
# print(ll)
# ll.add(2)
# print(ll)
# ll.add(1)
# print(ll)
# ll.remove(3)
# print(ll)
# ll.remove(1)
# print(ll)
# ll.remove(5)
# print(ll)
