# 런타임에러가 나서 찾아보니 재귀문제로 재귀 깊이를 늘려주면 된다고 함
import sys
sys.setrecursionlimit(10**9)

def dfs(node):
    for p in adj[node]:
        if not parent[p]:
            parent[p] = node
            dfs(p)


N = int(input())
tree = [[0] * (N+1) for _ in range(2)]
adj = [[] for _ in range(N+1)]
for n in range(N-1):
    x, y = map(int, input().split())
    if y not in adj[x]:
        adj[x].append(y)
    if x not in adj[y]:
        adj[y].append(x)

parent = [0] * (N+1)
dfs(1)
print(*parent[2:], sep='\n')
