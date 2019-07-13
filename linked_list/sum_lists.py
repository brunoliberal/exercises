from linked_list.likedlist import LinkedList, Node


# Sum two numbers represented by a linked list. The head of the list is the first right most
# digit of the number. Return the result of the sum as list.
# Space O(1). Time O(n)
def sum_lists(list_one, list_two):
    if not list_one.head or not list_two.head:
        return

    carry = 0
    aux1 = list_one.head
    aux1_prev = list_one.head
    aux2 = list_two.head

    while aux1 or aux2 or carry != 0:
        val1 = aux1.value if aux1 else 0
        val2 = aux2.value if aux2 else 0
        if not aux1:
            aux1_prev.next = Node((val1 + val2 + carry) % 10)
        else:
            aux1.value = (val1 + val2 + carry) % 10
        carry = 1 if val1 + val2 + carry >= 10 else 0
        aux1_prev = aux1 if aux1 else aux1_prev.next
        if aux1:
            aux1 = aux1.next
        if aux2:
            aux2 = aux2.next

    return list_one


first_ll = LinkedList(1)
first_ll.add(3)
first_ll.add(5)

second_ll = LinkedList(2)
second_ll.add(4)
second_ll.add(1)

# first_ll = LinkedList(9)
# first_ll.add(5)
# first_ll.add(1)
#
# second_ll = LinkedList(7)
# second_ll.add(4)
# second_ll.add(1)

# first_ll = LinkedList(2)
# first_ll.add(9)
#
# second_ll = LinkedList(8)
# second_ll.add(7)
# second_ll.add(9)
print(sum_lists(first_ll, second_ll))
