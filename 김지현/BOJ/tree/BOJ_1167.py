import sys
from collections import deque

def bfs(n):
    val = idx = 0
    visited = [0] * (V+1)
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for i, distance in adj[now]:
            if i != n and not visited[i]:
                visited[i] = visited[now] + distance
                q.append(i)
            if val < visited[i]:
                val, idx = visited[i], i
    return val, idx

V = int(sys.stdin.readline())
adj = [[]*(V+1) for _ in range(V+1)]
for i in range(V):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(temp)-1, 2):
        adj[temp[0]].append([temp[j], temp[j+1]])

max_V, node = bfs(1)
max_V, node = bfs(node)
print(max_V)