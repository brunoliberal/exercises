class Node:
    next = None
    prev = None

    def __init__(self, value):
        self.value = value


class DoubleLinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add(self, value):
        aux = self.head
        node = Node(value)
        if not aux:
            self.head = node
            return
        while aux.next:
            aux = aux.next
        aux.next = node
        node.prev = aux

    def remove(self, value):
        aux = self.head
        if not aux:
            return

        if aux.value == value:
            self.head = aux.next
            aux.next.prev = None
            return

        while aux.next:
            if aux.next.value == value:
                aux.next = aux.next.next
                if aux.next:
                    aux.next.prev = aux
                return
            aux = aux.next

    def __str__(self):
        aux = self.head
        values = []
        while aux:
            values.append(str(aux.value))
            aux = aux.next
        return ','.join(values)


# Tests:
# dll = DoubleLinkedList(5)
# print(dll)
# dll.add(4)
# print(dll)
# dll.add(3)
# print(dll)
# dll.add(2)
# print(dll)
# dll.add(1)
# print(dll)
# dll.remove(3)
# print(dll)
# dll.remove(1)
# print(dll)
# dll.remove(5)
# print(dll)
