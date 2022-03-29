import sys
from collections import deque

def bfs():
    q = deque()
    q.append(1)
    while q:
        n = q.popleft()
        for i in tree[n]:
            if ans[i] == 0:
                ans[i] = n
                q.append(i)


N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

ans = [0] * (N+1)
bfs()
for i in range(2, N+1):
    print(ans[i])
