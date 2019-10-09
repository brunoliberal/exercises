from collections import deque


class Order:
    def __init__(self, id, meta):
        self.id = id
        self.meta = meta

    def __str__(self):
        return self.id + self.meta


def prioritizedOrders(numOrders, orderList):
    sorted_order = deque()
    for o in orderList:  # loop at least one time through the list
        id = o.split()[0]
        meta = ' '.join(o.split()[2:])
        order = Order(id, meta)
        if meta.isdigit():  # if meta is digit append in the end in the order it came
            sorted_order.append(order)
        else:  # else check position to insert
            i = 0
            aux = []
            if sorted_order:
                while not sorted_order[i].id.isdigit() or order.meta > sorted_order[i].meta:
                    aux.append(sorted_order.popleft())
                    i += 1
                if order.meta == sorted_order[i + 1].meta and order.id > sorted_order[i + 1].id:
                    aux.append(sorted_order.popleft())
            sorted_order.appendleft(order)
            sorted_order.extendleft(aux)
    print(sorted_order)