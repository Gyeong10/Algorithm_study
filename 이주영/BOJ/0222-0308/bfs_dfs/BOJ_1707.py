# 인접배열 사용하니 메모리초과
# 두개의 정점이 오직 서로와만 연결되어 있는 경우를 생각해내는데 오래걸렸음
import sys
from collections import deque

def bfs(a, start, v):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in a[now]:
            if visited[i] == 0:
                visited[i] = -visited[now]
                q.append(i)
            else:
                if visited[now] == visited[i]:
                    return False
    return True


T = int(input())
for t in range(T):
    V, E = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    flag = 1
    for j in range(E):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    for k in range(1, V+1):
        if visited[k] == 0:
            if not bfs(arr, k, V):
                flag = 0
                break

    print('YES' if flag else 'NO')