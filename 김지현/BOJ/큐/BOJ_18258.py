import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for _ in range(N):
    s = sys.stdin.readline().split()

    if s[0] == 'push':
        Q.append(int(s[1]))
    elif s[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(Q))
    elif s[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)