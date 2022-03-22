# 2164 카드2

import sys
from collections import deque

sys.stdin = open('BOJ_2164.txt')

queue = deque()

N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    queue.append(i)

while len(queue) != 1:

    queue.pop()
    t = queue.pop()
    queue.appendleft(t)

print(*queue)