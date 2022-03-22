# 11866 요세푸스 문제 0

import sys
from collections import deque

sys.stdin = open('BOJ_11866.txt')

queue = deque()

N, K = map(int, sys.stdin.readline().split())
for i in range(1, N+1):
    queue.append(i)

print('<', end='')

cnt = 0
while len(queue) != 1:

    cnt += 1
    t = queue.popleft()

    if cnt == K:
        cnt = 0
        print(f'{t}, ', end='')
    else:
        queue.append(t)

print(f'{queue[0]}>')