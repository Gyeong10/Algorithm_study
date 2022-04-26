import sys; sys.stdin = open('BOJ_16562.txt')


def find(q):
    while q != parent[q]:
        q = parent[q]
    return q


def union(x, y):
    x = find(x)
    y = find(y)
    if A[x] < A[y]:
        parent[x] = y
        A[y] = A[x]
        A[x] = 0
    else:
        parent[y] = x
        A[x] = A[y]
        A[y] = 0


N, M, k = map(int, sys.stdin.readline().split())
A = list([0] + list(map(int, sys.stdin.readline().split())))
parent = list(range(N+1))

for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    union(v, w)

if sum(A) <= k:
    print(sum(A))
else:
    print('Oh no')