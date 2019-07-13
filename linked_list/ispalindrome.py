from linked_list.likedlist import LinkedList, Node


def equals(linked_list1, linked_list2):
    aux1 = linked_list1.head
    aux2 = linked_list2.head
    while aux1 and aux2:
        if not aux1 or not aux2 or aux1.value != aux2.value:
            return False
        aux1 = aux1.next
        aux2 = aux2.next
    return True


# Check is a linked list is a palindrome
# Space O(n). Time O(n)
def ispalindrome(linked_list):
    if not linked_list.head:
        return False

    aux = linked_list.head
    size = 0
    while aux:
        size += 1
        aux = aux.next

    if size == 1:  # maybe removed
        return True

    i = 1
    ll = None
    while i <= round(size/2):
        if not ll:
            ll = LinkedList(linked_list.head.value)
        else:
            new_head = Node(linked_list.head.value)
            new_head.next = ll.head
            ll.head = new_head
        if size % 2 == 0 or i != round(size/2):
            linked_list.head = linked_list.head.next
        i += 1

    return equals(ll, linked_list)


ll = LinkedList('a')
print(ispalindrome(ll))

ll = LinkedList('a')
ll.add('a')
print(ispalindrome(ll))

ll = LinkedList('t')
ll.add('a')
ll.add('c')
ll.add('c')
ll.add('a')
ll.add('t')
print(ispalindrome(ll))

ll = LinkedList('t')
ll.add('a')
ll.add('c')
ll.add('o')
ll.add('c')
ll.add('a')
ll.add('t')
print(ispalindrome(ll))

ll = LinkedList('a')
ll.add('b')
print(ispalindrome(ll))

ll = LinkedList('t')
ll.add('a')
ll.add('d')
ll.add('o')
ll.add('c')
ll.add('a')
ll.add('t')
print(ispalindrome(ll))

ll = LinkedList('t')
ll.add('a')
ll.add('c')
ll.add('d')
ll.add('a')
ll.add('t')
print(ispalindrome(ll))
