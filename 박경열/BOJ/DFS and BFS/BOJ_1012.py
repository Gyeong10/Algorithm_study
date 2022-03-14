# 1012 유기농 배추

import sys

def solve(i, j):
    global cnt
    queue = []
    queue.append([i, j])
    cnt += 1
    while queue:
        t = queue.pop()
        if not visited[t[0]][t[1]]:
            visited[t[0]][t[1]] = 1
        for a in range(4):
            if arr[t[0] + dy[a]][t[1] + dx[a]] and not visited[t[0] + dy[a]][t[1] + dx[a]]:
                queue.append([t[0] + dy[a], t[1] + dx[a]])


T = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * (M + 2) for _ in range(N + 2)]
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr[Y+1][X+1] = 1

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] and not visited[i][j]:
                solve(i, j)
    print(cnt)