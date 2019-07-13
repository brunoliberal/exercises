# Check if a given word is ONE edit from the other. Edit can be: 1 add, 1 delete or 1 change.


# Space O(N). Time O(N)
def str_shorter(word):
    short_word = []
    prev = None
    count = 1
    for c in word:
        if c == prev:
            count += 1
        else:
            if prev:
                short_word.append(count)
            short_word.append(c)
            count = 1
        prev = c
    short_word.append(count)

    return short_word if len(word) > len(short_word) else list(word)


print(str_shorter('aabcccccaaa'))  # a2b1c5a3
print(str_shorter('aaaaa'))  # a5
print(str_shorter('aaaaabbbbbccccc'))  # a5b5c5
print(str_shorter('aabbbc'))  # aabbbc
print(str_shorter('abc'))  # abc
print(str_shorter('a'))  # a

