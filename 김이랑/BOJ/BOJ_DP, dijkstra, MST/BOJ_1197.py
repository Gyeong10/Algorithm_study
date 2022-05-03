import heapq

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for i in range(E):
    A, B, C = map(int, input().split())
    edge[A].append([C, B])
    edge[B].append([C, A])

answer = 0
cnt = 0
heap = [[0, 1]]
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in edge[s]:
            heapq.heappush(heap, i)

print(answer)