import sys; sys.stdin = open('BOJ_4195.txt')


def find(v):
    while v != parent[v]:
        v = parent[v]
    return v


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        print(node[x])
        return

    if node[x] < node[y]:
        parent[x] = y
        node[y] += node[x]
        print(node[y])
    else:
        parent[y] = x
        node[x] += node[y]
        print(node[x])


def check(c):
    if c not in parent:
        parent[c] = c
        node[c] = 1


T = int(input())
for tc in range(T):
    F = int(input())
    parent = dict()
    node = dict()
    for i in range(F):
        s1, s2 = sys.stdin.readline().split()
        check(s1)
        check(s2)

        union(s1, s2)