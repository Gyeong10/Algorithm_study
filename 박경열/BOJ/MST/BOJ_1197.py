import sys; sys.stdin = open('BOJ_1197.txt')


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


V, E = map(int, sys.stdin.readline().split())
parent = list(range(V+1))
arr = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    arr.append([C, A, B])
arr.sort()

ans = 0
for a in arr:
    C, A, B = a

    if find(A) != find(B):
        union(A, B)
        ans += C
print(ans)