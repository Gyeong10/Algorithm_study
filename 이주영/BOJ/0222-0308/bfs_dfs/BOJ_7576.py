# 시간초과나서 input -> sys로 바꾸고 deque 사용
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]
deque = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            deque.append([i, j])
            visited[i][j] = 1
if len(deque) == N*M:
    deque.clear()
now = []
while deque:
    now = deque.popleft()
    for k in range(4):
        ni, nj = now[0] + di[k], now[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
            deque.append([ni, nj])
            arr[ni][nj] = 1
            visited[ni][nj] = visited[now[0]][now[1]] + 1

for line in arr:
    if 0 in line:
        print(-1)
        break
else:
    if now:
        print(visited[now[0]][now[1]] - 1)      # 처음부터 1이었던 것 카운트 하나 빼주기
    else:
        print(0)