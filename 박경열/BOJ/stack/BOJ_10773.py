# 10773 제로

import sys

K = int(sys.stdin.readline())

stack = [0]
for i in range(K):
    num = int(sys.stdin.readline())

    if num:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))