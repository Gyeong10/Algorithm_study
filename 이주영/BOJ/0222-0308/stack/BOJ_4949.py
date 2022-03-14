import sys
arr = []
bracket = {')': '(', ']': '['}
while True:
    arr.append(sys.stdin.readline().rstrip())
    if arr[-1] == '.':
        arr.pop()
        break
for sent in arr:
    stack = []
    top = 0
    flag = 1
    for i in range(len(sent)):
        if sent[i] == '(' or sent[i] == '[':
            top += 1
            stack.append(sent[i])
        elif sent[i] == ')' or sent[i] == ']':
            top -= 1
            if stack and stack[top] == bracket[sent[i]]:
                stack.pop()
            else:
                flag = 0
                break
    if flag and not stack:
        print('yes')
    else:
        print('no')

