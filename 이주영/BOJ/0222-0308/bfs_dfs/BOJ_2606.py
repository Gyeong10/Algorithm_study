N = int(input())    # N: 정점 수
M = int(input())    # M: 간선 수
arr = [list(map(int, input().split())) for _ in range(M)]
adj = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for line in arr:
    adj[line[0]][line[1]] = adj[line[1]][line[0]] = 1
stack = [1]
while stack:
    now = stack.pop()
    visited[now] = 1
    for i in range(1, N+1):
        if adj[now][i] and not visited[i]:
            stack.append(i)
print(visited.count(1)-1)
