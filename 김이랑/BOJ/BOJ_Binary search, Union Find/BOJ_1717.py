import sys
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())
parent = list(range(n+1))


def get_parent(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = get_parent(parent[a])
        return get_parent(parent[a])


def find(a, b):
    if get_parent(a) == get_parent(b):
        return 1
    return 0


def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

for i in range(m):
    order, a, b = map(int, input().split())
    if order:
        if find(a, b):
            print('YES')
        else:
            print('NO')

    else:
        union(a, b)