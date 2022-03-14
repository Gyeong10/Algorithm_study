# 1697 숨바꼭질

import sys
from collections import deque

def bfs():
    arr[N] = 1
    queue = deque()
    queue.append(N)
    while queue:
        t = queue.popleft()
        if t == K:
            return
        walk1 = t - 1
        if walk1 >= 0 and not arr[walk1]:
            queue.append(walk1)
            arr[walk1] = arr[t] + 1
        walk2 = t + 1
        if walk2 < 100001 and not arr[walk2]:
            queue.append(walk2)
            arr[walk2] = arr[t] + 1
        tel = t * 2
        if tel < 100001 and not arr[tel]:
            queue.append(tel)
            arr[tel] = arr[t] + 1


N, K = map(int, sys.stdin.readline().split())
arr = [0] * 100001
bfs()
print(arr[K]-1)