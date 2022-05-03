import sys; sys.stdin = open('BOJ_1922.txt')


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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = list(range(N+1))
arr = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([c, a, b])
arr.sort()
ans = 0

for values in arr:
    c, a, b = values

    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)