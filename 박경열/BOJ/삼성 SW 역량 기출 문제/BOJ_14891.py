# 14891 톱니바퀴

import sys; sys.stdin = open('BOJ_14891.txt')
from collections import deque

def solve(n, v):

    a, b = gears[n][2], gears[n][6]

    if v == 1:
        gear = gears[n].pop()
        gears[n].appendleft(gear)
    elif v == -1:
        gear = gears[n].popleft()
        gears[n].append(gear)

    visited[n] = 1

    if n-1 >= 0 and not visited[n-1] and gears[n-1][2] != b:
        solve(n-1, -v)
    if n+1 < 4 and not visited[n+1] and a != gears[n+1][6]:
        solve(n+1, -v)


# 2 6
gear1 = deque()
gear2 = deque()
gear3 = deque()
gear4 = deque()

for g in list(map(int, sys.stdin.readline().rstrip())):
    gear1.append(g)
for g in list(map(int, sys.stdin.readline().rstrip())):
    gear2.append(g)
for g in list(map(int, sys.stdin.readline().rstrip())):
    gear3.append(g)
for g in list(map(int, sys.stdin.readline().rstrip())):
    gear4.append(g)

gears = [gear1, gear2, gear3, gear4]

K = int(sys.stdin.readline())
for i in range(K):
    visited = [0] * 4
    n, v = map(int, sys.stdin.readline().split())

    solve(n-1, v)

ans = 0
for i in range(4):
    ans += gears[i][0] * (2 ** i)
print(ans)