def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N + 1):
        # 인접하고, 방문 안한 정점들이면,
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)


def bfs(a, v, start):   # a: 인접행렬, v : 정점의 개수, start : 탐색 시작점
    visit = [0] * (v + 1)
    q = []
    q.append(start)
    visit[start] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for w in range(1, v+1):
            if a[t][w] == 1 and visit[w] == 0:
                q.append(w)
                visit[w] = visit[t] + 1


N, M, V = map(int, input().split())     # N:정점의 개수  M: 간선의 개수 V: 시작 정점
arr = [list(map(int, input().split())) for _ in range(M)]
stack = [V]
visited = [0] * (N+1)
dfs_result = []
adj = [[0] * (N+1) for _ in range(N+1)]
for line in arr:
    adj[line[0]][line[1]] = adj[line[1]][line[0]] = 1

dfs(V)
print()
bfs(adj, N, V)





# while stack:
#     now = stack.pop()
#     dfs_result.append(now)
#     visited[now] = 1
#     for i in range(N, 0, -1):
#         if adj[now][i] == 1 and not visited[i]:
#             stack.append(i)
#     if len(dfs_result) == N:
#         break
# print(*dfs_result, sep=' ')

# bfs_result = []
# visited = [0] * (N+1)
# visited[V] = 1
# q = [V]
# while q:
#     now = q.pop(0)
#     bfs_result.append(now)
#     for i in range(1, N+1):
#         if adj[now][i] and not visited[i]:
#             q.append(i)
#             visited[i] = 1
# print(*bfs_result, sep=' ')