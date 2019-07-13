# Define if a word is a permutation of the other. Space: O(n). Time: O(nlogn)
def is_permutation_sort(word1, word2):
    return sorted(word1) == sorted(word2)


# Define if a word is a permutation of the other. Space O(1). Time: O(n^2)
def is_permutation(word1, word2):
    has_common = False
    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        for j in range(i, len(word2)):
            if word1[i] == word2[j]:
                word1[j] = '.'  # TODO: str doesnt support assign. transform in a list
                has_common = True
            if j == len(word2) and not has_common:
                return False
        has_common = False
    return True


# Define if a word is a permutation of the other. Space O(1). Time: O(n)
def is_permutation_hash(word1, word2):
    if len(word1) != len(word2):
        return False

    hash = [0] * 57  # ascii A = 65, z = 122
    for c in word1:
        hash[ord(c) - 65] += 1  # ascii A = 65
    for c in word2:
        hash[ord(c) - 65] -= 1
        if hash[ord(c) - 65] < 0:
            return False
    return True


word1, word2 = input('Type two words to check if one is a permutation of the other: \n').split()
print(is_permutation_sort(word1, word2))
print(is_permutation_hash(word1, word2))
# print(is_permutation(word1, word2))

# Hints:
# 1 - Describe what it means for two strings to be permutations of each other:
# If all characters in A are in B on a different order. Where sames characters show same amount of time.
# 84 - There is one solution that is 0( N log N) time. Another solution uses some space, but is O(N) time.
