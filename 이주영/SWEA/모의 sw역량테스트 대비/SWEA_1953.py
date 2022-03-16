from collections import deque
import sys

sys.stdin = open('1953_input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(x, y, cnt):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        nx, ny = q.popleft()
        if visited[nx][ny] == cnt:
            break
        for k in tunnel[arr[nx][ny]]:
            ni, nj = nx + di[k], ny + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                if (k+2)%4 not in tunnel[arr[ni][nj]]:
                    continue
                q.append([ni, nj])
                visited[ni][nj] = visited[nx][ny] + 1


T = int(input())

for t in range(1, T+1):
    N, M, X, Y, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    tunnel = [
        [],
        [0, 1, 2, 3],
        [0, 2],
        [1, 3],
        [0, 1],
        [1, 2],
        [2, 3],
        [0, 3]
    ]
    total = 0
    bfs(X, Y, time)
    for line in visited:
        for l in line:
            if l != 0:
                total += 1
    print(f'#{t} {total}')