# 10828 스택

import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    call = list(sys.stdin.readline().split())

    if call[0] == 'push':
        stack.append(call[1])

    if call[0] == 'pop':
        if stack:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)

    if call[0] == 'size':
        print(len(stack))

    if call[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    if call[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)