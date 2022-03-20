# 시간초과 나와서 sys.stdin.readline 사용
from collections import deque
import sys
N = int(sys.stdin.readline())
q = deque()
for n in range(N):
    arr = list(sys.stdin.readline().split())
    if len(arr) == 2:
        q.append(arr[1])
    else:
        if q and arr[0] == 'pop':
            print(q.popleft())
        elif arr[0] == 'size':
            print(len(q))
        elif arr[0] == 'empty':
            print(0 if q else 1)
        elif q and arr[0] == 'front':
            print(q[0])
        elif q and arr[0] == 'back':
            print(q[-1])
        else:
            print(-1)