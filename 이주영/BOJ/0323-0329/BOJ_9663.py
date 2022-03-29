# pypy3으로 해서 시간초과 해결..

def check(x):           # 같은 열이 있는지, 대각선에 있는지 확인
    for t in range(x):
        if row[t] == row[x] or abs(row[t] - row[x]) == abs(t - x):  # 대각선 상에 있는 경우 : 행 번호의 차이와 열 번호의 차이가 같은 경우
            return False
    return True

def n_queen(row_idx):
    global cnt
    if row_idx == N:
        cnt += 1
        return
    else:
        for i in range(N):
            row[row_idx] = i
            if check(row_idx):
                n_queen(row_idx+1)


N = int(input())
cnt = 0
row = [0] * N       # row[i] = j : [i, j]에 queen을 놓겠다
n_queen(0)
print(cnt)