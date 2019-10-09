MAX_CHAR = 10  # a-j = 0-9
ORD_A = 97


class Node:
    def __init__(self):
        self.next_n = [None for _ in range(MAX_CHAR)]
        self.end_w = False
        self.children_len = 0


class Trie:
    root = Node()

    def insert(self, w):
        aux = self.root
        for c in w:
            ord_rel = ord(c) - ORD_A
            if not aux.next_n[ord_rel]:
                aux.next_n[ord_rel] = Node()
                aux.children_len += 1
            aux = aux.next_n[ord_rel]
            if aux.end_w:
                return False
        if aux.children_len > 0:
            return False
        aux.end_w = True
        return True


# trie = Trie()
# result = 'GOOD SET'
#
# for word in ['aab', 'defgab','abcde','aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad']:
#     if not trie.insert(word):
#         result = 'BAD SET\n' + word
#         break
# print(result)
