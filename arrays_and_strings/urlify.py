# URLify a word. Replace spaces to '%20'.
# The word must have spaces that can fit the replacement.


# Time/Space O(N).
def urlify(word, size):
    word_url = [''] * len(word)
    j = 0
    for i in range(size):
        if word[i] == ' ':
            word_url[j] = '%'
            word_url[j + 1] = '2'
            word_url[j + 2] = '0'
            j += 2
        else:
            word_url[j] = word[i]
        j += 1
        i += 1
    return word_url


# Space O(1). Time O(N)
def urlify_lowspace(word):
    j = len(word) - 1
    letters_start = False
    for i in range(len(word) - 1, -1, -1):
        if word[i] != ' ':
            word[j] = word[i]
            letters_start = True
            j -= 1
        elif letters_start:
            word[j] = '0'
            word[j - 1] = '2'
            word[j - 2] = '%'
            j -= 3
    return word


word = list(input('Type a word to be URLify: \n'))
size = int(input('Type the word real size: \n'))
print(urlify(word, size))
print(urlify_lowspace(word))

# Best Conceivable Runtime = O(n). Must search word for spaces.
