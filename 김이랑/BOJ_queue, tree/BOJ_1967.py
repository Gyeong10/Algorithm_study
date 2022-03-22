from collections import deque
import sys

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    p, c, w = map(int, input().split())
    tree[p].append([w,c])
    tree[c].append([w,p])

def bfs(start):
    global max_node, max_dis

    queue = deque()
    depth = 0
    queue.append((start, depth))
    visited = [-1]*(N+1)
    visited[start] = 0

    max_depth = 0

    while queue:
        now, now_depth = queue.popleft()
        for i in range(len(tree[now])):
            dis = tree[now][i][0]
            next = tree[now][i][1]
            if visited[next] == -1:
                queue.append((next, now_depth+1))
                visited[next] = visited[now] + dis
                if max_dis <= visited[next]:
                    max_node = next
                    max_dis = visited[next]
                    max_depth = now_depth +1


max_node = 0
max_dis = 0

bfs(1)
bfs(max_node)

print(max_dis)