from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()
for n in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'push_front':
        q.appendleft(arr[1])
    elif arr[0] == 'push_back':
        q.append(arr[1])
    elif q and arr[0] == 'pop_front':
        print(q.popleft())
    elif q and arr[0] == 'pop_back':
        print(q.pop())
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
