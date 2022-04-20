from collections import deque
import sys

N = int(sys.stdin.readline())
edge = [[] for _ in range(N+1)]

for i in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    V = temp_list[0]
    j = 1
    while 1:
        if temp_list[j] == -1:
            break
        else:
            edge[V].append((temp_list[j], temp_list[j+1]))
            j+=2


def bfs(start):
    global max_total
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        now = queue.popleft()
        for i in range(len(edge[now])):
            next = edge[now][i][0]
            dis = edge[now][i][1]
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + dis
                if visited[next] > max_total:
                    max_total = visited[next]


max_total = 0
for i in range(1, N+1):
    visited = [-1] * (N+1)
    bfs(i)

print(max_total)