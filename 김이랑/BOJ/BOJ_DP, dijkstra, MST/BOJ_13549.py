import heapq

N, K = map(int, input().split())
MAX = 100001

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))

    times = [-1] * MAX
    times[n] = 0

    while queue:
        time, now = heapq.heappop(queue)
        next_pos = [now-1, now+1, now*2]
        if now == K:
            return times[now]
        for i in range(3):
            next = next_pos[i]
            if 0 <= next < MAX:
                if times[next] == -1 or times[next] > times[now]:
                    if i == 2:
                        heapq.heappush(queue, (time, next))
                        times[next] = time
                    else:
                        heapq.heappush(queue, (time+1, next))
                        times[next] = time+1

print(dijkstra(N))