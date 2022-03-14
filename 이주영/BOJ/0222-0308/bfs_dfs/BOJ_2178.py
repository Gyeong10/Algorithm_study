N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]
q = [(0, 0)]
visited[0][0] = 1
while q:
    now = q.pop(0)
    if now == (N-1, M-1):
        break
    for k in range(4):
        ni, nj = now[0] + di[k], now[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
            q.append((ni, nj))
            visited[ni][nj] = visited[now[0]][now[1]] + 1

print(visited[N-1][M-1])