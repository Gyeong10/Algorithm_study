import sys
n = int(sys.stdin.readline())
series = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
result = []
idx = 0

for i in range(1,n+1):
    while idx < n:
        stack.append(i)
        result.append('+')
        if i != series[idx]:
            break
        else:
            while stack[-1] == series[idx]:
                stack.pop()
                result.append('-')
                idx += 1
                if not stack:
                    break
            break

if stack:
    print('NO')
else:
    for i in result:
        print(i)