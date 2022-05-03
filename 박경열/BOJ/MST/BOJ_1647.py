import sys; sys.stdin = open('BOJ_1647.txt')


def find(v):
    while v != parent[v]:
        v = parent[v]
    return v


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


N, M = map(int, sys.stdin.readline().split())
parent = list(range(N+1))
arr = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([c, a, b])
arr.sort()
ans = []
for values in arr:
    c, a, b = values

    if find(a) != find(b):
        union(a, b)
        ans.append(c)

ans.pop()
print(sum(ans))