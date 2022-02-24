import sys
n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
result = []
cnt = 0
for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == arr[cnt]:
        stack.pop()
        result.append('-')
        cnt += 1

while stack and stack[-1] == arr[cnt]:
    result.append('-')
    stack.pop()
    cnt += 1
if stack:
    print('NO')
else:
    print(*result, sep='\n')