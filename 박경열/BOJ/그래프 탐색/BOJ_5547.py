import sys; sys.stdin = open('BOJ_5547.txt')
from collections import deque


def bfs(x, y):
    queue = deque()
    visited[x][y] = 1
    queue.append([x, y])

    flag = 0
    ssum = 0

    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[x % 2][i]
            ny = y + dy[x % 2][i]
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny]:
                    if arr[nx][ny]:
                        ssum += 1
                    else:
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
            else:
                flag = 1

    if flag:
        return ssum
    else:
        return 0


dx = [[-1, -1, 0, 1, 1, 0], [-1, -1, 0, 1, 1, 0]]
dy = [[0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1]]

W, H = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [[0] * W for _ in range(H)]
ans = 0

for i in range(H):
    for j in range(W):
        if not arr[i][j] and not visited[i][j]:
            ans += bfs(i, j)

        if i + 1 == H or i - 1 < 0 or j + 1 == W or j - 1 < 0:
            if arr[i][j]:
                for k in range(6):
                    nx = i + dx[i % 2][k]
                    ny = j + dy[i % 2][k]
                    if nx >= H or ny >= W or nx < 0 or ny < 0:
                        ans += 1

print(ans)

