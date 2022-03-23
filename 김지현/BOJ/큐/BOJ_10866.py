import sys
from collections import deque
Deque = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'push_front':
        Deque.appendleft(int(arr[1]))
    elif arr[0] == 'push_back':
        Deque.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if Deque:
            print(Deque.popleft())
        else:
            print(-1)
    elif arr[0] == 'pop_back':
        if Deque:
            print(Deque.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(Deque))
    elif arr[0] == 'empty':
        if Deque:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if Deque:
            print(Deque[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if Deque:
            print(Deque[-1])
        else:
            print(-1)
