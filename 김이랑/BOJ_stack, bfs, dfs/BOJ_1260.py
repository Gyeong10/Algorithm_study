from collections import deque

N, M, V = map(int, input().split())

edge = [[] for _ in range(N+1)]

for i in range(M):
    S, E = map(int, input().split())
    edge[S].append(E)
    edge[E].append(S)

for i in range(1, N+1):
    edge[i].sort()


def dfs(now):
    visited_DFS[now] = 1
    print(now, end=' ')
    for i in range(len(edge[now])):
        if visited_DFS[edge[now][i]] == 0:
            dfs(edge[now][i])


visited_DFS = [0] * (N+1)
dfs(V)
print()


def bfs(now):
    queue = deque()
    visited_BFS[now] = 1
    queue.append(now)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(len(edge[v])):
            if visited_BFS[edge[v][i]] == 0:
                visited_BFS[edge[v][i]] = 1
                queue.append(edge[v][i])


visited_BFS = [0] * (N+1)
bfs(V)