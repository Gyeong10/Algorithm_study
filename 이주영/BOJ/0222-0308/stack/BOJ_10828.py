import sys

stack = []
n = int(input())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]
for i in range(n):
    if arr[i][0] == 'push':
        stack.append(arr[i][1])
    elif arr[i][0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)