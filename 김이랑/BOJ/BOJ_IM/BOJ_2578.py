bingo_grid = [list(map(int, input().split())) for _ in range(5)]
answer_list = []

for _ in range(5):
    answer_list += input().split()


def bingo_check():
    total_line = 0
    for x in range(5):
        count_row = 0
        for y in range(5):
            if bingo_grid[x][y] == 0:
                count_row += 1
            if count_row == 5:
                total_line += 1

    for y in range(5):
        count_col = 0
        for x in range(5):
            if bingo_grid[x][y] == 0:
                count_col += 1
            if count_col == 5:
                total_line += 1

    count_diagonal = 0
    count_reverse_diagonal = 0

    for x in range(5):
        if bingo_grid[x][x] == 0:
            count_diagonal += 1
        if count_diagonal == 5:
            total_line += 1

        if bingo_grid[4-x][x] == 0:
            count_reverse_diagonal += 1
        if count_reverse_diagonal == 5:
            total_line += 1

    return total_line


def bingo_change(ans):
    for i in range(5):
        for j in range(5):
            if bingo_grid[i][j] == ans:
                bingo_grid[i][j] = 0
                return 0


total = 0
for _ in range(25):
    answer = int(answer_list[_])
    bingo_change(answer)
    # 와 대박 3이상이어야 하네ㅠㅠ
    if bingo_check() >= 3:
        total = _ + 1
        break

print(total)