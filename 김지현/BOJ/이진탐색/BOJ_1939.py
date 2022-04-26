import sys
from collections import deque

def bfs(x):
    queue = deque()
    queue.append(s)
    visited = [0] * (N+1)
    visited[s] = 1

    while queue:
        tmp = queue.popleft()
        if tmp == e:
            return True
        for v, w in graph[tmp]:
            if not visited[v] and w >= x:
                visited[v] = 1
                queue.append(v)
    return False

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s, e = map(int, sys.stdin.readline().split())

# 이진탐색으로 최댓값 찾기
left = 1
right = 1000000000
result = 0
while left <= right:
    mid = (left+right) // 2

    if bfs(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)


