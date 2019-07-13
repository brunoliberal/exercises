from linked_list.likedlist import LinkedList


# Partition a list between a given number x. Nodes less than x come
# before all nodes greater than or equal to x
# Space O(1). Time O(n)
def partition_list(linked_list, partition):
    if not linked_list.head or not linked_list.head.next:
        return

    aux = linked_list.head.next
    prev = linked_list.head
    while aux:
        if aux.value < partition:
            prev.next = aux.next
            aux.next = linked_list.head
            linked_list.head = aux
            aux = prev.next
        else:
            prev = aux
            aux = aux.next




# ll = LinkedList(1)
# ll.add(10)
# ll.add(2)
# ll.add(8)
# ll.add(7)
# ll.add(6)
# ll.add(2)
# partition_list(ll, 5)
# print(ll)


ll = LinkedList(5)
ll.add(3)
partition_list(ll, 4)
print(ll)
