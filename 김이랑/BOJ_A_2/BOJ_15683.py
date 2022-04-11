from copy import deepcopy

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

# 종류, 열좌표, 행좌표
cctv = []

for i in range(R):
    for j in range(C):
        if grid[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((grid[i][j]-1, i, j))

# 오른쪽, 아래, 왼쪽, 위
pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# CCTV 종류에 맞춰 인덱스 생성
cctv_pos = [[[0], [1], [2], [3]], [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)],
       [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)], [(0, 1, 2, 3)]]


def check(direction, r, c, check_grid):
    for i in range(len(direction)):
        now_r = r
        now_c = c
        while 0 <= now_r+pos[direction[i]][0] < R and 0 <= now_c+pos[direction[i]][1] < C:
            next_r = now_r+pos[direction[i]][0]
            next_c = now_c+pos[direction[i]][1]
            if check_grid[next_r][next_c] == 6:
                break
            elif check_grid[next_r][next_c] == 0:
                check_grid[next_r][next_c] = '#'
            now_r = next_r
            now_c = next_c


def dfs(prev_grid, D):
    global min_count
    if D == len(cctv):
        count = 0
        for i in range(R):
            for j in range(C):
                if prev_grid[i][j] == 0:
                    count += 1
        if count < min_count:
            min_count = count
    else:
        cctv_type, cctv_r, cctv_c = cctv[D]
        for i in range(len(cctv_pos[cctv_type])):
            copy_grid = deepcopy(prev_grid)
            check(cctv_pos[cctv_type][i], cctv_r, cctv_c, copy_grid)
            dfs(copy_grid, D+1)


min_count = 1000
dfs(grid, 0)

print(min_count)