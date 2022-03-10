from collections import deque
import sys

cols, rows = map(int, sys.stdin.readline().split())
grid = [list(map(int, input())) for _ in range(cols)]
visited = [[0] * rows for _ in range(cols)]
checked = [[0] * rows for _ in range(cols)]

pos_i = [0, 1, 0, -1]
pos_j = [1, 0, -1, 0]

def bfs():
    queue = deque()
    queue.append([0,0])
    checked[0][0] = 1
    visited[0][0] = 1
    while queue:
        now = queue.popleft()
        for _ in range(4):
            next_i = now[0] + pos_i[_]
            next_j = now[1] + pos_j[_]
            if 0<=next_i<cols and 0<=next_j<rows:
                if grid[next_i][next_j] == 1 and visited[next_i][next_j] == 0:
                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = 1
                    checked[next_i][next_j] = checked[now[0]][now[1]] + 1



bfs()
print(checked[cols-1][rows-1])