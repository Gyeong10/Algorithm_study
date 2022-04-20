from collections import deque
cols, rows = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(rows)]

visited = [[0] * rows for _ in range(rows)]
checked = [[0] * rows for _ in range(rows)]

pos_i = [0, 1, 0, -1]
pos_j = [1, 0, -1, 0]
queue = deque()

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            queue.append([i,j])
count = 0
max = 0
while queue:
    now = queue.popleft()
    for i in range(4):
        next_row = now[0] + pos_i[i]
        next_col = now[1] + pos_j[i]
        if 0<= next_row < rows and 0<= next_col < cols:
            if grid[next_row][next_col] == 0:
                grid[next_row][next_col] = grid[now[0]][now[1]] + 1
                queue.append([next_row, next_col])
flag = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            max = -1
            flag = 1
            break
        elif grid[i][j] - 1 > max:
            max = grid[i][j] - 1
    if flag:
        break

print(max)