from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
q = deque([i+1 for i in range(N)])
cnt = 0
for i in arr:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2:
                    q.append(q.popleft())
                    cnt += 1
            else:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)