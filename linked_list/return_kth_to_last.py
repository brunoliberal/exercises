from linked_list.likedlist import LinkedList


# Return the kth to last element of a singly linked list.
# Space O(1). Time O(n)
def return_kth_to_last(linked_list, kth):
    if not linked_list.head:
        return None

    aux = linked_list.head
    size = 0
    while aux:
        aux = aux.next
        size += 1

    if kth >= size:
        return
    complement = size - kth

    aux = linked_list.head
    i = 1
    while i != complement:
        aux = aux.next
        i += 1
    return aux.value


ll = LinkedList(5)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)

ll_one_elem = LinkedList(1)

print(return_kth_to_last(ll, 1))
print(return_kth_to_last(ll, 2))
print(return_kth_to_last(ll, 3))
print(return_kth_to_last(ll, 4))
print(return_kth_to_last(ll, 5))
print(return_kth_to_last(ll, 6))

print(return_kth_to_last(ll_one_elem, 0))
print(return_kth_to_last(ll_one_elem, 1))
