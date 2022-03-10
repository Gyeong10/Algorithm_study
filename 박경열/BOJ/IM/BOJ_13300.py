# 방 배정

import sys

def up(n, m):
    if n % m != 0:
        return n//m + 1
    else:
        return n//m

students = [[0]*2 for _ in range(6)]

N, K = map(int, sys.stdin.readline().split())

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    students[Y-1][S] += 1

ans = 0
for i in range(6):
    ans += up(students[i][0], K)
    ans += up(students[i][1], K)

print(ans)