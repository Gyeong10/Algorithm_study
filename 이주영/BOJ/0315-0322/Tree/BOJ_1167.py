# 인접행렬 사용하니 메모리초과해서 [연결정점, 거리]를 리스트로 해서 사용
# input 사용하니 시간초과해서 sys 사용
# 트리의 지름은 아무 노드에서 bfs(dfs도 무관)를 통해 가정 멀리있는 노드를 구한 후 해당 노드에서 bfs를 한번더 진행하여 가장 멀리있는 노드를 구하면 된다.
import sys

def bfs(n):
    val = idx = 0
    visited = [0] * (V+1)
    q = []
    q.append(n)
    while q:
        now = q.pop(0)
        for k, power in adj[now]:
            if k != n and not visited[k]:
                visited[k] = visited[now] + power
                q.append(k)
            if val < visited[k]:
                val, idx = visited[k], k
    return val, idx


V = int(sys.stdin.readline())
tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(V)]
adj = [[] * (V+1) for _ in range(V+1)]

for line in tmp:
    for i in range(1, len(line)-1, 2):
        adj[line[0]].append([line[i], line[i+1]])

max_val, node = bfs(1)
max_val, node = bfs(node)
print(max_val)

