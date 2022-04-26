N, K = map(int, input().split())

row_cal = 0
col_cal = N-(N//2)

flag = 1
while row_cal <= col_cal:
    mid_cal = (row_cal+col_cal)//2
    col = N//2 + mid_cal
    row = N - col
    cut = (row+1)*(col+1)

    if cut == K:
        print('YES')
        flag = 0
        break
    elif cut > K:
        row_cal = mid_cal + 1
    else:
        col_cal = mid_cal - 1

if flag:
    print('NO')