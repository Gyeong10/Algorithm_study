import sys; sys.stdin = open('BOJ_1976.txt')


def find(v):
    while v != parent[v]:
        v = parent[v]
    return v


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = list(range(N+1))
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(len(maps)):
    for j in range(len(maps)):
        if maps[i][j]:
            union(i, j)

path = list(map(int, sys.stdin.readline().split()))
flag = 1
for i in range(M - 1):
    if find(path[i]-1) != find(path[i+1] - 1):
        flag = 0
        break

print('YES' if flag else 'NO')