# 1874 스택 수열

import sys

n = int(sys.stdin.readline())
arr = list(range(n, 0, -1))
stack = []
ans = []

comp = [0]*n
for i in range(n):
    comp[i] = int(sys.stdin.readline())

answer = []
x = 0
while comp != ans:
    if stack and stack[-1] == comp[x]:
        ans.append(stack[-1])
        stack.pop()
        x += 1
        answer.append('-')
    elif not arr:
        answer = ['NO']
        break
    else:
        stack.append(arr[-1])
        arr.pop()
        answer.append('+')

for a in answer:
    print(a)