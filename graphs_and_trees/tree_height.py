class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    if not root.left and not root.right:
        return 0
    height_left = 0
    height_right = 0
    if root.left:
        height_left = 1 + height(root.left)

    if root.right:
        height_right = 1 + height(root.right)

    return height_left if height_left > height_right else height_right


# tree = BinarySearchTree()
# t = int(input())
#
# arr = list(map(int, input().split()))
#
# for i in range(t):
#     tree.create(arr[i])
#
# print(height(tree.root))
