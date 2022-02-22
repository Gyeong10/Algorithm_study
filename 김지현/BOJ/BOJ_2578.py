def check_bingo(arr1, arr2):
    cnt = [0]*12
    bingo = 0
    n = 0
    for i in range(5):
        for j in range(5):
            n += 1
            for k in range(5):
                for l in range(5):
                    # 숫자가 일치하면 0으로 바꿈
                    if arr1[k][l] == arr2[i][j]:
                        arr1[k][l] = 0
                        cnt[k] += 1
                        cnt[l+5] += 1
                        #대각선
                        if k == l:
                            cnt[10] += 1
                        if k == 4 - l :
                            cnt[11] += 1
                        for m in range(12):
                            if cnt[m] == 5:
                                bingo += 1
                                cnt[m] = 0
                                if bingo == 3:
                                    return n


a = [list(map(int, input().split())) for _ in range(5)]
b = [list(map(int, input().split())) for _ in range(5)]
print(check_bingo(a,b))