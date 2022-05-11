# 시간 초과.. visited를 append형식이 아닌 2차원 배열로 만드니 통과
import sys

d = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direct = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for drt in direct:
    visited = [[0] * N for _ in range(N)]
    ncloud = []
    di, si = drt
    for c in cloud:
        x = (c[0] + (d[di][0] * si)) % N
        y = (c[1] + (d[di][1] * si)) % N
        arr[x][y] += 1
        visited[x][y] = 1
        ncloud.append([x, y])
    for c in ncloud:
        cnt = 0
        for i in range(2, 9, 2):
            ni, nj = c[0] + d[i][0], c[1] + d[i][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                cnt += 1
        arr[c[0]][c[1]] += cnt
    cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                cloud.append([i, j])
                arr[i][j] -= 2

ans = 0
for rr in arr:
    ans += sum(rr)
print(ans)