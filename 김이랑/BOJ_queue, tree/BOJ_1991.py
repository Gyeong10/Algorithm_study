
N_input = int(input())
N = 27
tree = [[] for _ in range(N+1)]

for i in range(N_input):
    temp = list(map(str, input().split()))
    for j in range(3):
        if temp[j] != '.':
            temp[j] = ord(temp[j]) - 64

    tree[temp[0]].append(temp[1])
    tree[temp[0]].append(temp[2])


def pre_order(v):
    if v <= N:
        print(chr(v+64), end='')
        if tree[v]:
            if tree[v][0] != '.':
                pre_order(tree[v][0])
            if tree[v][1] != '.':
                pre_order(tree[v][1])


pre_order(1)
print()


def in_order(v):
    if v <= N:
        if tree[v] and tree[v][0] != '.':
            in_order(tree[v][0])
        print(chr(v+64), end='')
        if tree[v] and tree[v][1] != '.':
            in_order(tree[v][1])


in_order(1)
print()


def post_order(v):
    if v <= N:
        if tree[v]:
            if tree[v][0] != '.':
                post_order(tree[v][0])
            if tree[v][1] != '.':
                post_order(tree[v][1])
        print(chr(v+64), end='')


post_order(1)