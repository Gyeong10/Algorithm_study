from collections import deque

pos_r = [1, 1, -1, -1]
pos_c = [1, -1, -1, 1]


def check(row, col, total, direction):
    global max_total

    next_row = row + pos_r[direction]
    next_col = col + pos_c[direction]

    if 0<=next_row<N and 0<=next_col<N:
        if grid[next_row][next_col] not in number:
            number.append(grid[next_row][next_col])
            check(next_row, next_col, total+1, direction)
            number.pop()
            if direction < 3 and grid[row][col] not in changed:
                changed.append(grid[row][col])
                check(row, col, total, direction+1)
                changed.pop()
        elif grid[next_row][next_col] in number:
            if next_row == i and next_col == j and direction == 3:
                # total += 1
                if total > max_total:
                    max_total = total
            elif direction < 3 and (grid[row][col] not in changed):
                changed.append(grid[row][col])
                check(row, col, total, direction+1)
                changed.pop()
    else:
        if direction < 3 and grid[row][col] not in changed:
            changed.append(grid[row][col])
            check(row, col, total, direction+1)
            changed.pop()
        else:
            total = -1
            if total > max_total:
                max_total = total


for test_case in range(1, int(input())+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_total = -1

    for i in range(0, N-2):
        for j in range(1, N-1):
            number = [grid[i][j]]
            changed = []
            check(i, j, 1, 0)

    print(f'#{test_case} {max_total}')