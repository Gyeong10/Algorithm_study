# 1260 DFS와 BFS

import sys

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    if sum(visited) == N:
        return

    for w in range(1, N+1):
        if arr[v][w] == 1 and not visited[w]:
            dfs(w)


def bfs(v):
    visit = [0] * (N + 1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visit[t]:
            visit[t] = 1
            print(t, end=' ')
        for x in range(1, N+1):
            if arr[t][x] and not visit[x]:
                queue.append(x)


N, M, V = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e] = 1
    arr[e][s] = 1

visited = [0] * (N+1)
dfs(V)
print('')
bfs(V)

