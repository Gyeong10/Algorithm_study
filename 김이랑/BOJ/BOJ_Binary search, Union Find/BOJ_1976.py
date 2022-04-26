N = int(input())
M = int(input())

parent = list(range(N))


def get_parent(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = get_parent(parent[a])
        return get_parent(parent[a])


def find(a, b):
    if get_parent(a) == get_parent(b):
        return 1
    else:
        return 0


def union(a, b):
    p_a = get_parent(a)
    p_b = get_parent(b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b


for i in range(N):
    connect = list(map(int, input().split()))
    for j in range(N):
        if connect[j]:
            union(i, j)

tours = list(map(int, input().split()))
answer = get_parent(tours[0]-1)

for tour in tours:
    tour -= 1
    if get_parent(tour) != answer:
        print('NO')
        break
else:
    print('YES')

