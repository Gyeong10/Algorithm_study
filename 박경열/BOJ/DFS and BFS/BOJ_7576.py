# 7576 토마토

import sys
from collections import deque

def tomato(arr):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 1:
                queue.append([i, j])


def bfs():
    global ans
    while queue:
        t = queue.popleft()
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            if not arr[nx][ny] and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[t[0]][t[1]] + 1
            if visited[nx][ny] > ans:
                ans = visited[nx][ny]


M, N = map(int, sys.stdin.readline().split())
arr = [[-1] * (M+2)] + [[-1] + list(map(int, sys.stdin.readline().split())) + [-1] for _ in range(N)] + [[-1] * (M+2)]
visited = arr[:]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()

ans = 1
tomato(arr)
bfs()
for i in range(1, N+1):
    if 0 in visited[i]:
        ans = 0
        break

print(ans-1)