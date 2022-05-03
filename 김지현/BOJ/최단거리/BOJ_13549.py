from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [-1 for _ in range(100001)]
visited[N] = 0

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break
    if 0 <= now - 1 < 100001 and visited[now-1] == -1:
        visited[now-1] = visited[now] + 1
        q.append(now-1)
    if 0 <= 2*now < 100001 and visited[2*now] == -1:
        visited[2*now] = visited[now]
        q.appendleft(2*now)
    if 0 <= now + 1 < 100001 and visited[now+1] == -1:
        visited[now+1] = visited[now] + 1
        q.append(now+1)
