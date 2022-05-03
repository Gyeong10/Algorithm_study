import sys
import heapq

V, E = map(int, input().split())
INF = int(1e9)
start = int(input())
edge = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    edge[u].append((v, w))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dis, now = heapq.heappop(queue)
        if distance[now] < dis:
            continue

        for next in edge[now]:
            cost = dis + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))


dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])