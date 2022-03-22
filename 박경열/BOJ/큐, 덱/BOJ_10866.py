# 10866 덱

import sys
from collections import deque

sys.stdin = open('BOJ_10866.txt')

queue =deque()

N = int(sys.stdin.readline())
for _ in range(N):
    T = list(sys.stdin.readline().split())

    if T[0] == 'push_front':
        queue.appendleft(int(T[1]))

    if T[0] == 'push_back':
        queue.append(int(T[1]))

    if T[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if T[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)

    if T[0] == 'size':
        print(len(queue))

    if T[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    if T[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if T[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)