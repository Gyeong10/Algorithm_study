import sys

N = int(sys.stdin.readline())

parent = list(range(10**6+1))
size = [1]*(10**6+1)


def get_parent(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = get_parent(parent[a])
        return parent[a]


def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    # 부모가 이미 같은 경우가 있을 수 있음
    if parent_a < parent_b:
        parent[parent_b] = parent_a
        size[parent_a] += size[parent_b]
        size[parent_b] = 0
    elif parent_b < parent_a:
        parent[parent_a] = parent_b
        size[parent_b] += size[parent_a]
        size[parent_a] = 0


for i in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'I':
        union(int(order[1]), int(order[2]))
    elif order[0] == 'Q':
        check = get_parent(int(order[1]))
        print(size[check])