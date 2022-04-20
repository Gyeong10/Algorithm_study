grid_j, grid_i = map(int, input().split())
grid = [[1]*(grid_j+1)]+[([1]+[0]*(grid_j-1)+[1]) for _ in range(grid_i-1)]+[[1]*(grid_j+1)]

case_num = int(input())
for _ in range(case_num):
    check, cut = map(int, input().split())

    if check:
        for i in range(1, grid_i+1):
            grid[i][cut] += 1
    else:
        for j in range(1, grid_j+1):
            grid[cut][j] += 1

max_row = -1
max_col = -1

count = 1
for i in range(1, grid_i+1):
    for j in range(1, grid_j+1):
        if grid[i][j] == 0:
            count += 1
        else:
            if count > max_row:
                max_row = count
            count = 1

for j in range(1, grid_j+1):
    for i in range(1, grid_i+1):
        if grid[i][j] == 0:
            count += 1
        else:
            if count > max_col:
                max_col = count
            count = 1

print(max_row*max_col)