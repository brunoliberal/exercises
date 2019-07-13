from linked_list.likedlist import LinkedList, Node


# Check is a linked lists contains a loop. Return the node at beginning of loop.
# Space O(n). Time O(n)
def loop_detect(linked_list):
    if not linked_list.head:
        return

    dict = {}
    aux = linked_list.head
    while aux:
        if dict.get(aux):
            return aux
        dict[aux] = 1
        aux = aux.next


circular_ll = LinkedList('A')
circular_ll.add('B')
circular_ll.add('C')
circular_ll.add('D')
circular_ll.add('E')
tail = circular_ll.head.next.next.next.next
node_c = circular_ll.head.next.next
tail.next = node_c
print(loop_detect(circular_ll))

not_circular_ll = LinkedList('A')
not_circular_ll.add('B')
not_circular_ll.add('C')
not_circular_ll.add('D')
not_circular_ll.add('E')
print(loop_detect(not_circular_ll))
