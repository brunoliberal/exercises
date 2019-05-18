# Check if a given word is ONE edit from the other. Edit can be: 1 add, 1 delete or 1 change.

# Space O(1). Time O(N)
def is_one_edit(word1, word2):
    if len(word1) != len(word2) and abs(len(word1) - len(word2)) != 1:
        return False

    hash = [0] * 57
    for c in word1:
        hash[ord(c) - 65] += 1
    for c in word2:
        if hash[ord(c) - 65] == 0:
            hash[ord(c) - 65] += 1
        else:
            hash[ord(c) - 65] -= 1

    i = 0
    for c in hash:
        i += c

    if i in (1, 2):
        return True
    return False


print(is_one_edit('pale', 'palesi'))  # False
print(is_one_edit('pale', 'pa'))  # False
print(is_one_edit('pale', 'ple'))  # True
print(is_one_edit('pales', 'pale'))  # True
print(is_one_edit('pale', 'bale'))  # True
print(is_one_edit('pale', 'bake'))  # False
print(is_one_edit('ppppp', 'pppppp'))  # True
print(is_one_edit('ppppp', 'pppp'))  # True
print(is_one_edit('ppppp', 'pppap'))  # True
