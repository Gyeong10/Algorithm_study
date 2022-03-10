N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
stack = [V]
visited = [0] * (N+1)
dfs_result = []
bfs_result = []
adj = [[0] * (N+1) for _ in range(N+1)]
for line in arr:
    adj[line[0]][line[1]] = adj[line[1]][line[0]] = 1
while stack:
    now = stack.pop()
    dfs_result.append(now)
    visited[now] = 1
    for i in range(N, 0, -1):
        if adj[now][i] == 1 and not visited[i]:
            stack.append(i)
print(dfs_result)