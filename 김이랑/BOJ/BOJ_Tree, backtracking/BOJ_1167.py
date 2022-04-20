import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    s = temp_list[0]
    i = 1
    while 1:
        if temp_list[i] == -1:
            break
        else:
            e = temp_list[i]
            dis = temp_list[i+1]
            tree[s].append((e, dis))
            i += 2


def bfs(start):
    global max_dis, max_idx
    visited = [-1] * (N+1)
    queue = deque()
    visited[start] = 0
    queue.append((start,0))

    while queue:
        now, now_dis = queue.popleft()
        for next in tree[now]:
            if visited[next[0]] == -1:
                visited[next[0]] = visited[now] + next[1]
                queue.append(next)

    for i in range(1, N+1):
        if visited[i] > max_dis:
            max_dis = visited[i]
            max_idx = i


max_idx = max_dis = -1
#1에서 가장 먼 노드
bfs(1)
bfs(max_idx)

print(max_dis)