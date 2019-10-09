import os

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s) % 2 == 1: return 'NO'
    stack = []
    for bracket in s:
        if bracket in ['{', '(', '[']:
            stack.append(bracket)
        elif stack:
            if bracket == '}' and stack.pop() != '{':
                return 'NO'
            elif bracket == ')' and stack.pop() != '(':
                return 'NO'
            elif bracket == ']' and stack.pop() != '[':
                return 'NO'
        else:
            return 'NO'
    return 'YES' if not stack else 'NO'


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         s = input()
#
#         result = isBalanced(s)
#
#         fptr.write(result + '\n')
#
#     fptr.close()
