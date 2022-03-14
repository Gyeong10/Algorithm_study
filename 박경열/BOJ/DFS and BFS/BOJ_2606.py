# 2606 바이러스

import sys

# dfs
def dfs(v):
    visited[v] = 1

    for w in range(1, N+1):
        if arr[v][w] and not visited[w]:
            dfs(w)

# bfs
def bfs(v):
    visit = [0] * (N + 1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visit[t]:
            visit[t] = 1
        for x in range(1, N+1):
            if arr[t][x] and not visit[x]:
                queue.append(x)

    return sum(visit)-1


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e] = 1
    arr[e][s] = 1


print(bfs(1))

visited = [0] * (N + 1)
dfs(1)
print(sum(visited)-1)

