# Check if a given work is a permutation of a palindrome. Spaces allowed.


# Space O(1). Time O(n)
def is_palindrome_perm(word):
    hash = [0] * 57
    for c in word:
        if c != ' ':
            hash[ord(c) - 65] += 1
    i = 0
    for c in hash:
        i += c % 2
    if i > 1:
        return False
    return True


# word = list(input('Type a word to check is it is a permutation of a palindrome: \n'))

print(is_palindrome_perm('tacocat'))
print(is_palindrome_perm('tact coa'))
print(is_palindrome_perm('taccat'))
print(is_palindrome_perm('ccatat'))
print(is_palindrome_perm('ccc'))
print(is_palindrome_perm('abcaacba'))
print(is_palindrome_perm('ccca'))
print(is_palindrome_perm('abcabccd'))
