# 미완성
import sys

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = []
    visited = []
    for i in range(N-2):
        for j in range(1, N-1):
            start.append([i, j])
    for point in start:
        stack = [point]
        # x = y = 0
        while stack:
            x, y = stack.pop()
            visited.append(arr[x][y])
            print(f'x, y : {x},{y}')
            if x < N-1 and 0 < y and arr[x+1][y-1] not in visited:
                visited.append(arr[x+1][y-1])
                stack.append([x+1, y-1])
                print(f'[x+1, y-1] : {x + 1},{y - 1}')

            if x < N-1 and y < N-1 and arr[x+1][y+1] not in visited:
                visited.append(arr[x + 1][y + 1])
                stack.append([x + 1, y + 1])
                print(f'[x+1, y+1] : {x + 1},{y + 1}')
