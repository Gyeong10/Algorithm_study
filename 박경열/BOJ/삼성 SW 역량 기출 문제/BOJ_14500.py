# 14500 테트로미노
import sys; sys.stdin = open('BOJ_14500.txt')


def solve(x, y, k, ssum):
    global ans

    if k == 3:
        if ans < ssum:
            ans = ssum
        return

    if ans >= ssum + (3 - k) * MAX:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not used[nx][ny]:
                used[nx][ny] = 1
                if k == 1:
                    solve(x, y, k+1, ssum + arr[nx][ny])
                solve(nx, ny, k+1, ssum + arr[nx][ny])
                used[nx][ny] = 0


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]

ans = 0
MAX = max(map(max, arr))
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        used[i][j] = 1
        solve(i, j, 0, arr[i][j])
        used[i][j] = 0

print(ans)