from linked_list.likedlist import LinkedList


# Remove duplications from a linked list
# Space O(1). Time O(n²)
def remove_dup(linked_list):
    first = linked_list.head

    while first and first.next:
        second = first
        while second.next:
            if first.value == second.next.value:
                second.next = second.next.next
            else:
                second = second.next
        first = first.next


ll = LinkedList(5)
ll.add(4)
ll.add(3)
ll.add(5)
ll.add(4)
ll.add(3)

print(ll)
remove_dup(ll)
print(ll)
