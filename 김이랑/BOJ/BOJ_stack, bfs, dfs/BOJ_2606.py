vertex = int(input())
edge_num = int(input())
edge = [[] for _ in range(vertex+1)]


for i in range(edge_num):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

visited = [0]*(vertex+1)


def dfs(now):
    global count
    count += 1
    visited[now] = 1
    for i in range(len(edge[now])):
        if visited[edge[now][i]] == 0:
            dfs(edge[now][i])

count = 0
dfs(1)
print(count-1)

