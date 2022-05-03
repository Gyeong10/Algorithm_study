import sys
import heapq
# from collections import deque
def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    # q = deque([0, start])
    while heap:
        weight, now = heapq.heappop(heap)
        # weight, now = q.popleft()
        if dp[now] < weight:
            continue
        for w, next in arr[now]:
            next_w = w + weight
            if next_w < dp[next]:
                dp[next] = next_w
                heapq.heappush(heap, (next_w, next))
                # q.append([next_w, next])


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = sys.maxsize
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append([w, v])
visited = [0] * (V+1)
dp = [INF] * (V+1)
heap = []
dijkstra(K)
for i in range(1, V+1):
    print(dp[i] if dp[i] != INF else "INF")