# 포문돌면서 1을 하나씩 수정하고 BFS 가기
# flag 만들어서 한번만 1을 0으로 만들어보기

from collections import deque
import sys
import copy

cols, rows = map(int, sys.stdin.readline().split())
grid = [list(map(int, input())) for _ in range(cols)]
visited = [[0] * rows for _ in range(cols)]
checked = [[0] * rows for _ in range(cols)]
temp_grid = [[0] * rows for _ in range(cols)]
temp_visited = [[0] * rows for _ in range(cols)]
temp_checked = [[0] * rows for _ in range(cols)]
changed =  [[0] * rows for _ in range(cols)]
pos_i = [0, 1, 0, -1]
pos_j = [1, 0, -1, 0]

def bfs(checked, visited, grid):
    queue = deque()
    temp_queue = deque()
    queue.append([0,0])
    checked[0][0] = 1
    visited[0][0] = 1
    flag = 1
    while queue:
        now = queue.pop()
        for _ in range(4):
            next_i = now[0] + pos_i[_]
            next_j = now[1] + pos_j[_]
            if 0<=next_i<cols and 0<=next_j<rows:
                if grid[next_i][next_j] == 0 and visited[next_i][next_j] == 0:
                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = 1
                    checked[next_i][next_j] = checked[now[0]][now[1]] + 1
                elif flag and grid[next_i][next_j] == 1 and visited[next_i][next_j] == 0 and changed[next_i][next_j] == 0 :
                    temp_queue = copy.deepcopy(queue)
                    temp_visited = copy.deepcopy(visited)
                    temp_checked = copy.deepcopy(checked)
                    temp_grid = copy.deepcopy(grid)
                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = 1
                    checked[next_i][next_j] = checked[now[0]][now[1]] + 1
                    changed[next_i][next_j] = 1
                    flag = 0
                elif flag == 0 and grid[next_i][next_j] == 1 and visited[next_i][next_j] == 0:
                    visited = temp_visited
                    checked = temp_checked
                    grid = temp_grid
                    queue = temp_queue
                    flag = 1

bfs(checked, visited, grid)
if checked[cols-1][rows-1] == 0:
    print(-1)
else :
    print(checked[cols-1][rows-1])

print(changed)
print(checked)