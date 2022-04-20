from collections import deque
import sys

N = int(sys.stdin.readline())
edge = [[] for _ in range(N+1)]

start = 0
large = 0
real_start = 0

for i in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    V = temp_list[0]

    if len(temp_list) == 4:
        if large < temp_list[2]:
            large = temp_list[2]
            start = temp_list[1]
            real_start = temp_list[0]

    j = 1
    while 1:
        if temp_list[j] == -1:
            break
        else:
            edge[V].append((temp_list[j], temp_list[j+1]))
            j+=2


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = large
    while queue:
        now = queue.popleft()
        for i in range(len(edge[now])):
            next = edge[now][i][0]
            dis = edge[now][i][1]
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + dis


max_total = 0
visited = [-1] * (N+1)
bfs(start)

for i in range(len(visited)):
    if max_total < visited[i] and i != real_start:
        max_total = visited[i]

print(max_total)