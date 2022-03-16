import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
result = []
length = N

while q:
    for i in range(K-1):
        tmp = q.popleft()
        q.append(tmp)
    result.append(q.popleft())
    length -= 1
print('<', end='')
print(*result, sep=', ', end='')
print('>')
