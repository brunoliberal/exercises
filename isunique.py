# Define if a word have unique characters or not. Time/Space: O(n)
def is_unique(word):
    str_dict = set()  # dict with dummy values. hashtable!
    for c in word:
        if c in str_dict:
            return False
        str_dict.add(c)
    return True


# Implementation without additional data structures. Space: O(1). Time: O(n²)
def is_unique_low_space(word):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True


string = input('Type a string to check if has all uniques characters: \n')
print(is_unique(string))
print(is_unique_low_space(string))
