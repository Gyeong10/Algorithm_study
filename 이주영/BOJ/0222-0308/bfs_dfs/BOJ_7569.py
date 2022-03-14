import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N*K)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N*K)]
deque = deque()

for i in range(N*K):
    for j in range(M):
        if arr[i][j] == 1:
            deque.append([i, j])
            visited[i][j] = 1

if len(deque) == N*M*K:
    deque.clear()

now = []
while deque:
    now = deque.popleft()
    for t in range(4):
        ni, nj = now[0] + di[t], now[1] + dj[t]
        if (now[0]//N)*N <= ni < (now[0]//N)*N+N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
            deque.append([ni, nj])
            arr[ni][nj] = 1
            visited[ni][nj] = visited[now[0]][now[1]] + 1
    for k in [-1, 1]:
        ni, nj = now[0] + (k*N), now[1]
        if 0 <= ni < (N*K) and not arr[ni][nj] and not visited[ni][nj]:
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