# 예외가 왜있져
from collections import deque

def dfs(prev, now):
    global count

    if visited[now] == 0:
        visited[now] = 1
        for i in range(len(edge[now])):
            next = edge[now][i]
            if visited[next] == 0:
                dfs(now, next)
            elif visited[next] and next != prev:
                count = -1

case = 0
while 1:
    case += 1
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    if V == 0:
        break
    for i in range(E):
        start, end = map(int, input().split())
        edge[start].append(end)
        edge[end].append(start)

    visited = [0] * (V+1)
    count = 0
    for i in range(1, V+1):
        if visited[i] == 0:
            count += 1
            start = i
            dfs(0, i)
        if count == -1:
            break

    print(f'Case {case}: ', end='')
    if count == -1:
        print('No trees.')
    elif count == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {count} trees.')