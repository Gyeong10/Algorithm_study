# 빙고
c_arr = [list(map(int, input().split())) for _ in range(5)]
h_arr = []
for _ in range(5):
    h_arr += list(map(int, input().split()))
bingo = [[0] * 5 for _ in range(5)]
cnt = 0
for k in range(25):
    row = 0
    flag = 0
    for i in range(5):
        for j in range(5):
            if h_arr[k] == c_arr[i][j]:
                bingo[i][j] = 1
                cnt += 1
                flag = 1
                break
        if flag == 1:
            break
    # 가로
    for i in range(5):
        if bingo[i] == [1] * 5:
            row += 1
    # 대각선\
    for i in range(5):
        if bingo[i][i] == 0:
            break
    else:
        row += 1
    # 세로
    for i in range(5):
        for j in range(5):
            if bingo[j][i] == 0:
                break
        else:
            row += 1
    # 대각선/
    for i in range(5):
        if bingo[i][4-i] == 0:
            break
    else:
        row += 1
    # 빙고 3줄 이상인지 확인
    if row >= 3:
        break

print(cnt)