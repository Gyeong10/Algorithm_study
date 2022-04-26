import sys; sys.stdin = open('BOJ_18116.txt')


def find(v):
    while v != parent[v]:
        v = parent[v]
    return v


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if robot[x] < robot[y]:
        parent[x] = y
        robot[y] += robot[x]
    else:
        parent[y] = x
        robot[x] += robot[y]


N = int(sys.stdin.readline())
parent = list(range(10**6 + 1))
robot = [1] * (10**6 + 1)

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'I':
        union(int(arr[1]), int(arr[2]))
    else:
        x = find(int(arr[1]))
        print(robot[x])