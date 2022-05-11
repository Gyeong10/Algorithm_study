import sys; sys.stdin = open('BOJ_14502.txt')
from collections import deque
import copy


def bfs():
    global ans

    arr_visited = [[0] * M for _ in range(N)]
    arr_temp = copy.deepcopy(arr)

    queue = deque()
    for i in vi:
        queue.append(i)

    while queue:
        x, y = queue.popleft()
        arr_visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not arr_temp[nx][ny]:
                arr_temp[nx][ny] = 2
                arr_visited[nx][ny] = 1
                queue.append([nx, ny])

    ssum = 0
    for i in range(N):
        for j in range(M):
            if not arr_temp[i][j]:
                ssum += 1

    if ssum > ans:
        ans = ssum


def solve(cnt):
    global l

    if cnt == 3:
        bfs()
        return

    for i in range(l):
        if not visited[i]:
            visited[i] = 1
            arr[blank[i][0]][blank[i][1]] = 1
            solve(cnt + 1)
            arr[blank[i][0]][blank[i][1]] = 0
            visited[i] = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0

blank = []
vi = deque()
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            blank.append([i, j])

        if arr[i][j] == 2:
            vi.append([i, j])


l = len(blank)
visited = [0] * l
solve(0)

print(ans)