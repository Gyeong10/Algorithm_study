import sys
from collections import deque
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    q = deque()
    cnt = 0
    for i in range(N):
        q.append([i, arr[i]])
    while q:
        max_val = max(r[1] for r in q)
        if max_val == q[0][1]:
            now = q.popleft()
            cnt += 1
            if now[0] == M:
                print(cnt)
                break
        else:
            tmp = q.popleft()
            q.append(tmp)
