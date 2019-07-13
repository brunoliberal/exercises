from linked_list.likedlist2 import LinkedList


class AnimalShelter:
    dogs = LinkedList()
    cats = LinkedList()

    # Time O(n). Space O(1)
    def enqueue(self, name, type):
        if name:
            if type == 'dog':
                self.dogs.add(name)
                self.cats.add(None)
            elif type == 'cat':
                self.cats.add(name)
                self.dogs.add(None)

    # Time O(n). Space O(1)
    def dequeue(self, type):
        if type == 'dog':
            stk_sch, stk_rm = self.dogs, self.cats
        else:
            stk_sch, stk_rm = self.cats, self.dogs
        aux_s, aux_r = stk_sch.head, stk_rm.head

        if aux_s and aux_s.value:  # maybe use a method in list to remove from idx (don't exist yet)
            stk_rm.remove()
            return stk_sch.remove()

        while aux_s.next and not aux_s.next.value:
            aux_s, aux_r = aux_s.next, aux_r.next

        if aux_s.next and aux_s.next.value:
            v = aux_s.next.value
            aux_s.next, aux_r.next = aux_s.next.next, aux_r.next.next
            return v

    # Time O(1). Space O(1)
    def dequeueAny(self):
        dog = self.dogs.remove()
        cat = self.cats.remove()
        return dog if dog else cat

    def __str__(self):
        return 'dogs:' + str(self.dogs) + ' cats:' + str(self.cats)


# Tests:
# shelter = AnimalShelter()
# shelter.enqueue('Bobby', 'dog')
# shelter.enqueue('Mingau', 'cat')
# shelter.enqueue('Branco', 'dog')
# shelter.enqueue('Pretinha', 'dog')
#
# print(shelter)
# print(shelter.dequeue('cat'))
# print(shelter)
# print(shelter.dequeue('dog'))
# print(shelter)
# print(shelter.dequeueAny())
# print(shelter)
# print(shelter.dequeueAny())
# print(shelter)
# print(shelter.dequeueAny())


