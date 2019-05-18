# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring.


# Space O(n). Time O(n)
def isrotation(s1, s2):
    if len(s1) != len(s2):
        return False
    word = s1 + s1
    return s2 in word


print(isrotation('waterbottle', 'erbottlewat'))

