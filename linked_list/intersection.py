import copy

from linked_list.likedlist import LinkedList, Node


# Check is two linked lists intersect (by reference). Return the intersection node.
# Space O(1). Time O(n+m)
def intersection(first_list, second_list):
    if not first_list.head or not second_list.head:
        return

    first_size = 0
    aux = first_list.head
    while aux:
        first_size += 1
        aux = aux.next

    second_size = 0
    aux = second_list.head
    while aux:
        second_size += 1
        aux = aux.next

    aux1 = first_list.head
    aux2 = second_list.head
    if first_size > second_size:
        while first_size != second_size:
            aux1 = aux1.next
            first_size -= 1
    elif second_size > first_size:
        while second_size != first_size:
            aux2 = aux2.next
            second_size -= 1

    while aux1 and aux2:
        if aux1 == aux2:
            return aux1
        aux1 = aux1.next
        aux2 = aux2.next

    return


first_ll = LinkedList('1')
first_ll.add('2')
first_ll.add('3')
first_ll.add('4')
first_ll.add('5')

second_ll = copy.copy(first_ll)
second_ll.head = second_ll.head.next
new_head = Node(9)
new_head.next = second_ll.head.next
second_ll.head = new_head
print(intersection(first_ll, second_ll))
