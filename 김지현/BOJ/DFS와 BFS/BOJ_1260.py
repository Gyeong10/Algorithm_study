def dfs(n):
    visited[n] = 1
    result.append(n)
    for m in range(1, N+1):
        if adj[n][m] == 1 and visited[m] == 0:
            dfs(m)

def bfs(n):
    Q = []
    visited[n] = 1
    Q.append(n)
    result.append(n)
    while Q:
        n = Q.pop(0)
        for m in range(1,N+1):
            if adj[n][m] == 1 and visited[m] == 0:
                Q.append(m)
                visited[m] = 1
                result.append(m)
    

N, M, V = map(int, input().split())

# 인접행렬
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

# DFS
visited = [0] * (N+1)
result = []
dfs(V)
print(*result)

# BFS
visited = [0] * (N+1)
result = []
bfs(V)
print(*result)

