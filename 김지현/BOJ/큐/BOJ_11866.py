import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
Q = deque([i for i in range(1,N+1)])
result = '<'
idx = 0
while len(Q) > 1:
    idx += 1
    if idx % K == 0:
        result += f'{Q.popleft()}, '
    else:
        Q.append(Q.popleft())
result += f'{Q.popleft()}>'
print(result)