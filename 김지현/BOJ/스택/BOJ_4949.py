import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s[0] == '.' and len(s) == 1:
        break
    
    stack = []

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                stack.append(i)
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                stack.append(i)
                break
            else:
                stack.pop()
    
    if stack:
        print('no')
    else:
        print('yes')