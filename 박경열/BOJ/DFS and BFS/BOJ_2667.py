# 2667 단지번호붙이기

import sys

def solve(i, j):
    global cnt
    visited[i][j] = 1
    cnt += 1

    for a in range(4):
        if arr[i+dy[a]][j + dx[a]] and not visited[i+dy[a]][j + dx[a]]:
            solve(i + dy[a], j + dx[a])


N = int(sys.stdin.readline())
arr = [[0] * (N+2)] + [[0] + list(map(int, sys.stdin.readline().rstrip())) + [0] for _ in range(N)] + [[0] * (N+2)]
visited = [[0]*(N+2) for _ in range(N+2)]

ans = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(1, N+1):
    for j in range(1, N+1):
        cnt = 0
        if arr[i][j] and not visited[i][j]:
            solve(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for s in ans:
    print(s)