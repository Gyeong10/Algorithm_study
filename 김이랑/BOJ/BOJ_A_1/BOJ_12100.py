from copy import deepcopy

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
# 4방향 으로 만들 수 있는 중복 순열 생성
direction = [0, 0, 0, 0, 0]


def move(dir, temp_grid):
    # 오른쪽으로 이동
    if dir == 0:
        for i in range(N):
            # value, row, cal
            temp = [-1, -1, -1]
            for j in range(N-1, -1, -1):
                if temp_grid[i][j] == temp[0]:
                    temp_grid[temp[1]][temp[2]] += temp[0]
                    temp_grid[i][j] = 0
                    temp = [-1, -1, -1]
                else:
                    if temp_grid[i][j] != 0:
                        temp = [temp_grid[i][j], i, j]

            cnt = N-1
            for j in range(N-1, -1, -1):
                if temp_grid[i][j]:
                    temp_grid[i][cnt] = temp_grid[i][j]
                    if cnt != j:
                        temp_grid[i][j] = 0
                    cnt -= 1

    # 밑으로 이동
    elif dir == 1:
        for j in range(N):
            # value, row, cal
            temp = [-1, -1, -1]
            for i in range(N-1, -1, -1):
                if temp_grid[i][j] == temp[0]:
                    temp_grid[temp[1]][temp[2]] += temp[0]
                    temp_grid[i][j] = 0
                    temp = [-1, -1, -1]
                else:
                    if temp_grid[i][j] != 0:
                        temp = [temp_grid[i][j], i, j]

            cnt = N-1
            for i in range(N-1, -1, -1):
                if temp_grid[i][j]:
                    temp_grid[cnt][j] = temp_grid[i][j]
                    if cnt != i:
                        temp_grid[i][j] = 0
                    cnt -= 1

    # 왼쪽 이동
    if dir == 2:
        for i in range(N):
            # value, row, cal
            temp = [-1, -1, -1]
            for j in range(N):
                if temp_grid[i][j] == temp[0]:
                    temp_grid[temp[1]][temp[2]] += temp[0]
                    temp_grid[i][j] = 0
                    temp = [-1, -1, -1]
                else:
                    if temp_grid[i][j] != 0:
                        temp = [temp_grid[i][j], i, j]

            cnt = 0
            for j in range(N):
                if temp_grid[i][j]:
                    temp_grid[i][cnt] = temp_grid[i][j]
                    if cnt != j:
                        temp_grid[i][j] = 0
                    cnt += 1

    # 위로 이동
    elif dir == 3:
        for j in range(N):
            # value, row, cal
            temp = [-1, -1, -1]
            for i in range(N):
                if temp_grid[i][j] == temp[0]:
                    temp_grid[temp[1]][temp[2]] += temp[0]
                    temp_grid[i][j] = 0
                    temp = [-1, -1, -1]
                else:
                    if temp_grid[i][j] != 0:
                        temp = [temp_grid[i][j], i, j]

            cnt = 0
            for i in range(N):
                if temp_grid[i][j]:
                    temp_grid[cnt][j] = temp_grid[i][j]
                    if cnt != i:
                        temp_grid[i][j] = 0
                    cnt += 1

    return temp_grid


def combination(D):
    global max_value
    if D == 5:
        check_grid = deepcopy(grid)
        for i in range(5):
            check_grid = move(direction[i], check_grid)

        for i in range(N):
            for j in range(N):
                if max_value < check_grid[i][j]:
                    max_value = check_grid[i][j]

    else:
        for i in range(4):
            direction[D] = i
            combination(D+1)


max_value = 0
combination(0)

print(max_value)

