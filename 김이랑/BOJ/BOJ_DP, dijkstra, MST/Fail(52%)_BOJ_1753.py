V, E = map(int, input().split())
INF = int(1e9)
start = int(input())
edge = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    edge[u].append((v, w))


def get_smallest_node():
    min = INF
    idx = 0
    for i in range(1, V+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in range(len(edge[start])):
        distance[edge[start][i][0]] = edge[start][i][1]

    for _ in range(V-1):
        now = get_smallest_node()
        visited[now] = True
        for j in range(len(edge[now])):
            temp = distance[now] + edge[now][j][1]
            if temp < distance[edge[now][j][0]]:
                distance[edge[now][j][0]] = temp


dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])