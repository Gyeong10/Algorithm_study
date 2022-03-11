import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([i for i in range(1,N+1)])

while len(Q) > 1:
    Q.popleft()
    if len(Q) == 1:
        break
    Q.append(Q.popleft())

print(*Q)