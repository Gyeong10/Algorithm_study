from collections import deque

N, K = map(int, input().split())
cnt = [0] * 1000001
q = deque()
q.append(N)

while q:
    now = q.popleft()
    if now == K:
        break
    for ni in [now-1, now+1, now*2]:
        if 0 <= ni <= 1000000 and not cnt[ni]:
            cnt[ni] = cnt[now] + 1
            q.append(ni)

print(cnt[K])