import sys

def BFS(node):
    mmax = [0, 0]      # [최대합, 더한 노드중 마지막 노드]
    visited = [0] * (N + 1)
    q = []
    q.append(node)
    while q:
        now = q.pop(0)
        for n, power in lines[now]:
            if n != node and not visited[n]:
                visited[n] = visited[now] + power
                q.append(n)
            if mmax[0] < visited[n]:
                mmax = [visited[n], n]
    return mmax


N = int(sys.stdin.readline())
tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
lines = [[] for _ in range(N+1)]

# mmax = [0, 0]
for row in tmp:
    lines[row[0]].append([row[1], row[2]])
    lines[row[1]].append([row[0], row[2]])

ans, nnode = BFS(1)
ans, nnode = BFS(nnode)
print(ans)