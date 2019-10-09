class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None for i in range(27)]  # not sure if this works


class PrefixTrie:
    def __init__(self):
        self.root = Node('.')

    def addword(self, word):
        aux = self.root
        for letter in word:
            letter_num = ord(letter) - 97
            if not aux.children[letter_num]:
                aux.children[letter_num] = Node(1)
            else:
                aux.children[letter_num].value += 1
            aux = aux.children[letter_num]

    def occurences(self, prefix):
        if len(prefix) == 0: return 0

        aux = self.root
        for letter in prefix:
            letter_num = ord(letter) - 97
            if not aux.children[letter_num]:
                return 0
            aux = aux.children[letter_num]
        return aux.value


#
# Complete the contacts function below.
#
def contacts(queries):
    trie = PrefixTrie()
    for query in queries:
        cmd, string = query
        if cmd == 'add':
            trie.addword(string)
        elif cmd == 'find':
            yield trie.occurences(string)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     queries_rows = int(input())
#
#     queries = []
#
#     for _ in range(queries_rows):
#         queries.append(input().rstrip().split())
#
#     result = contacts(queries)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
