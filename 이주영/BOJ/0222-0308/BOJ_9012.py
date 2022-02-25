import sys

n = int(input())
arr = [sys.stdin.readline() for _ in range(n)]
for t in range(n):
    stack = []
    flag = 1
    for i in range(len(arr[t])-1):
        if arr[t][i] == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                flag = 0
                break
    if flag and not stack:
        print('YES')
    else:
        print('NO')