import sys

stack = []
k = int(input())
arr = [int(sys.stdin.readline()) for _ in range(k)]
for i in range(k):
    if arr[i] == 0:
        stack.pop()
    else:
        stack.append(arr[i])
print(sum(stack))