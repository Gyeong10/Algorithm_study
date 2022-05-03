import sys
import heapq

def dijkstra(start):
    heapq.heappush(heap, (0, start))
    dp[start] = 0
    while heap:
        time, now = heapq.heappop(heap)
        if now == K:
            break
        for x in [now-1, now+1]:
            if 0 <= x <= 100_000 and dp[x] > time + 1:
                dp[x] = time + 1
                heapq.heappush(heap, (time+1, x))
        if now*2 <= 100_000 and dp[now*2] > time:
            dp[now*2] = time
            heapq.heappush(heap, (time, now*2))



N, K = map(int, sys.stdin.readline().split())
dp = [100001] * 100_001
heap = []
dijkstra(N)
print(dp[K])