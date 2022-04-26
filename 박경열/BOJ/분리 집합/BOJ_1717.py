import sys; sys.stdin = open('BOJ_1717.txt')


def find(v):
    while v != parent[v]:
        v = parent[v]
    return v


def union(x, y):
    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] = y
    else:
        parent[y] = x


n, m = map(int, sys.stdin.readline().split())
parent = list(range(n+1))

for i in range(m):
    s, a, b = map(int, sys.stdin.readline().split())

    if not s:
        x = find(a)
        y = find(b)
        union(x, y)

    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')