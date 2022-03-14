from collections import deque

di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for t in range(T):
    N = int(input())
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))
    visited = [[0] * N for _ in range(N)]
    q = deque([knight])
    visited[knight[0]][knight[1]] = 1
    while q:
        now = q.popleft()
        for k in range(8):
            ni, nj = now[0] + di[k], now[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = visited[now[0]][now[1]] + 1
        if visited[target[0]][target[1]] != 0:
            break
    print(visited[target[0]][target[1]] - 1)
