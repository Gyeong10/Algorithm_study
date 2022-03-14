# 1949 등산로 조성

def high():
    h = []
    w = 0
    for x in range(N):
        if max(arr[x]) > w:
            w = max(arr[x])

    for x in range(N):
        for y in range(N):
            if arr[x][y] == w:
                h.append([x, y])

    return h

def bfs():
    global ans
    visited = [[0] * N for _ in range(N)]
    for q in queue:
        visited[q[0]][q[1]] = 1

    while queue:
        t = queue.pop(0)
        for d in range(4):
            nx = t[0] + dx[d]
            ny = t[1] + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] < arr[t[0]][t[1]]:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[t[0]][t[1]] + 1
                if visited[nx][ny] > ans:
                    ans = visited[nx][ny]


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ans = 0
    for k in range(1, K+1):
        for i in range(N):
            for j in range(N):
                queue = high()
                arr[i][j] -= k
                bfs()
                arr[i][j] += k

    print(f'#{tc+1} {ans}')