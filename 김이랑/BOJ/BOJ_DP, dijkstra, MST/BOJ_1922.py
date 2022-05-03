import heapq

N = int(input())
M = int(input())
edge = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((c, b))
    edge[b].append((c, a))

answer = 0
cnt = 0
heap = []
heapq.heappush(heap, [0, 1])

while heap:
    if cnt == N:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        for i in edge[s]:
            heapq.heappush(heap, i)

print(answer)