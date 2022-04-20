from collections import deque

row, col = map(int, input().split())
grid = [list(map(str, input())) for _ in range(row)]

blue, red, hole = [], [], []

for i in range(row):
    for j in range(col):
        if grid[i][j] == 'B':
            grid[i][j] = '.'
            blue = [i, j]
        elif grid[i][j] == 'R':
            grid[i][j] = '.'
            red = [i, j]
        elif grid[i][j] == 'O':
            hole = [i, j]


def move(direction, ball, another_ball):
    now_r = ball[0]
    now_c = ball[1]

    pos_r = pos[direction][0]
    pos_c = pos[direction][1]

    while 1:
        next_r = now_r + pos_r
        next_c = now_c + pos_c
        if grid[next_r][next_c] == '.':
            if not (next_r == another_ball[0] and next_c == another_ball[1]):
                now_r = next_r
                now_c = next_c
                continue
        if grid[next_r][next_c] == 'O':
            return -1, -1
        else:
            return now_r, now_c


pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start_b, start_r, start_cnt, start_direction):
    global answer

    queue = deque()
    queue.append((start_b, start_r, start_cnt, start_direction))

    # 0, 2번은 아래위로 - col확인, 1, 3번은 양옆으로 - row 확인
    while queue:
        b, r, cnt, direction = queue.popleft()

        if b == [-1, -1]:
            continue
        elif r == [-1, -1]:
            if cnt < answer:
                answer = cnt
            continue
        elif cnt >= answer:
            continue
        elif cnt == 10:
            continue

        for i in range(4):
            if i == direction:
                continue
            flag = 0 #블루 움직이고, 레드 움직임
            if r[1] == b[1]:
                if i == 0 and r[0] > b[0]:
                    flag = 1
                elif i == 2 and r[0] < b[0]:
                    flag = 1
            elif r[0] == b[0]:
                if i == 1 and r[1] > b[1]:
                    flag = 1
                elif i == 3 and r[1] < b[1]:
                    flag = 1

            # 빨강 먼저
            if flag:
                r_row, r_col = move(i, r, b)
                new_r = [r_row, r_col]
                b_row, b_col = move(i, b, new_r)
                new_b = [b_row, b_col]
            else:
                b_row, b_col = move(i, b, r)
                new_b = [b_row, b_col]
                r_row, r_col = move(i, r, new_b)
                new_r = [r_row, r_col]

            if r == new_r and b == new_b:
                continue
            else:
                queue.append((new_b, new_r, cnt+1, i))


answer = 11
bfs(blue, red, 0, -1)

if answer == 11:
    answer = -1

print(answer)