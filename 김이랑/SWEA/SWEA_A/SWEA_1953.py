from collections import deque

pos_r_1 = [0, 1, 0, -1]
pos_c_1 = [1, 0, -1, 0]

pos_r_2 = [-1, 1]

pos_r_4 = [0, -1]
pos_c_4 = [1, 0]

pos_r_5 = [0, 1]
pos_c_5 = [1, 0]

pos_r_6 = [1, 0]
pos_c_6 = [0, -1]

pos_r_7 = [0, -1]
pos_c_7 = [-1, 0]


for test_case in range(1, int(input())+1):
    rows, cols, r, c, time = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    visited = [[0]*cols for _ in range(rows)]

    queue = deque()
    visited[r][c] = 1
    queue.append((r, c))
    count = 1

    def visit(now_r, now_c, next_r, next_c):
        global queue
        visited[next_r][next_c] = visited[now_r][now_c] + 1
        queue.append((next_r, next_c))

    while queue:

        if count == time+1:
            break

        now_r, now_c = queue.popleft()
        type = grid[now_r][now_c]

        if type == 1:
            for i in range(4):
                next_r = now_r + pos_r_1[i]
                next_c = now_c + pos_c_1[i]
                if 0<=next_r<rows and 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 3, 6, 7]:
                            visit(now_r, now_c, next_r, next_c)
                    if visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 2, 4, 7]:
                            visit(now_r, now_c, next_r, next_c)
                    if visited[next_r][next_c] == 0 and i == 2:
                        if grid[next_r][next_c] in [1, 3, 4, 5]:
                            visit(now_r, now_c, next_r, next_c)
                    if visited[next_r][next_c] == 0 and i == 3:
                        if grid[next_r][next_c] in [1, 2, 5, 6]:
                            visit(now_r, now_c, next_r, next_c)

        elif type == 2:
            for i in range(2):
                next_r = now_r + pos_r_2[i]
                next_c = now_c
                if 0<=next_r<rows:
                    # 위로갈떄
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 2, 5, 6]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 2, 4, 7]:
                            visit(now_r, now_c, next_r, next_c)
        elif type == 3:
            for i in range(2):
                next_r = now_r
                next_c = now_c + pos_r_2[i]
                if 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 3, 4, 5]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 3, 6, 7]:
                            visit(now_r, now_c, next_r, next_c)
        elif type == 4:
            for i in range(2):
                next_r = now_r + pos_r_4[i]
                next_c = now_c + pos_c_4[i]
                if 0<=next_r<rows and 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 3, 6, 7]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 2, 5, 6]:
                            visit(now_r, now_c, next_r, next_c)
        elif type == 5:
            for i in range(2):
                next_r = now_r + pos_r_5[i]
                next_c = now_c + pos_c_5[i]
                if 0<=next_r<rows and 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 3, 6, 7]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 2, 4, 7]:
                            visit(now_r, now_c, next_r, next_c)
        elif type == 6:
            for i in range(2):
                next_r = now_r + pos_r_6[i]
                next_c = now_c + pos_c_6[i]
                if 0<=next_r<rows and 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 2, 4, 7]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 3, 4, 5]:
                            visit(now_r, now_c, next_r, next_c)
        elif type == 7:
            for i in range(2):
                next_r = now_r + pos_r_7[i]
                next_c = now_c + pos_c_7[i]
                if 0<=next_r<rows and 0<=next_c<cols:
                    if visited[next_r][next_c] == 0 and i == 0:
                        if grid[next_r][next_c] in [1, 3, 4, 5]:
                            visit(now_r, now_c, next_r, next_c)
                    elif visited[next_r][next_c] == 0 and i == 1:
                        if grid[next_r][next_c] in [1, 2, 5, 6]:
                            visit(now_r, now_c, next_r, next_c)

    total = 0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] != 0 and visited[i][j] <= time:
                total += 1

    print(f'#{test_case} {total}')