from collections import deque

w, h = map(int, input().split())
arr = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    arr[i][1:w+1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0 for _ in range(w+2)] for _ in range(h+2)]
    visited[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[y % 2][i]
            if 0 <= ny < h+2 and 0 <= nx < w+2:
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                elif arr[ny][nx] == 1:
                    cnt += 1
    return cnt

print(bfs(0, 0))