def dfs(v):
    global cnt
    visited[v] = 1
    cnt += 1
    for w in range(1,N+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

N = int(input())
V = int(input())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(V):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

visited = [0]*(N+1)
cnt = 0
dfs(1)
print(cnt-1)