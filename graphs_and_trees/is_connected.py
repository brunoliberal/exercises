from stacks_and_queues.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)


def is_connected(node_from, node_to):
    if not node_from or not node_to:
        return False

    queue = Queue()

    for node in node_from.children:
        if node == node_to:
            return True
        queue.add(node)

    while not queue.is_empty():
        cur_node = queue.remove().value
        for node in cur_node.children:
            if node == node_to:
                return True
            queue.add(node)
    return False


# Tests:
node7 = Node(7)
node6 = Node(6)
node5 = Node(5)
node5.children = [node6, node7]
node4 = Node(4)
node3 = Node(3)
node3.children = [node4, node5]
node2 = Node(2)
node2.children = [node3]
node1 = Node(1)
node1.children = [node2]
print(is_connected(node1, node7))  # True
print(is_connected(node3, node1))  # False
