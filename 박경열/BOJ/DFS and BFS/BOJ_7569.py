# 7569 토마토

import sys
from collections import deque

def tomato(arr):
    for k in range(1, H+1):
        for i in range(1, N+1):
            for j in range(1, M+1):
                if arr[k][i][j] == 1:
                    queue.append([k, i, j])


def bfs():
    global ans
    while queue:
        t = queue.popleft()
        for i in range(4):
            nx = t[1] + dx[i]
            ny = t[2] + dy[i]
            if not arr[t[0]][nx][ny] and not visited[t[0]][nx][ny]:
                queue.append([t[0], nx, ny])
                visited[t[0]][nx][ny] = visited[t[0]][t[1]][t[2]] + 1
            if visited[t[0]][nx][ny] > ans:
                ans = visited[t[0]][nx][ny]
        for i in range(2):
            nz = t[0] + dz[i]
            if not arr[nz][t[1]][t[2]] and not visited[nz][t[1]][t[2]]:
                queue.append([nz, t[1], t[2]])
                visited[nz][t[1]][t[2]] = visited[t[0]][t[1]][t[2]] + 1
            if visited[nz][t[1]][t[2]] > ans:
                ans = visited[nz][t[1]][t[2]]


M, N, H = map(int, sys.stdin.readline().split())
arr = [[[-1] * (M+2)]*(N+2)] + [0] * H + [[[-1] * (M+2)]*(N+2)]
for h in range(1, H+1):
    arr[h] = [[-1] * (M+2)] + [[-1] + list(map(int, sys.stdin.readline().split())) + [-1] for _ in range(N)] + [[-1] * (M+2)]

visited = arr[:]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [1, -1]
queue = deque()

ans = 1
tomato(arr)
bfs()
for j in range(1, H+1):
    for i in range(1, N+1):
        if 0 in visited[j][i]:
            ans = 0
            break

print(ans-1)