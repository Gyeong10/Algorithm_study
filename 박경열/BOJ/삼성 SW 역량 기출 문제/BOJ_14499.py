# 14499 주사위 굴리기

import sys; sys.stdin = open('BOJ_14499.txt')

def roll(n):

    Es = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
    Ws = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
    So = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
    No = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]

    r = [Es, Ws, No, So]
    return r[n]


N, M, x, y, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))

# 아래 동 서 남 북 위
dice = [0] * 6

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for o in order:
    if 0 <= x + dx[o-1] < N and 0 <= y + dy[o-1] < M:
        x, y = x + dx[o-1], y + dy[o-1]
        dice = roll(o - 1)
        if not arr[x][y]:
            arr[x][y] = dice[0]
        else:
            dice[0] = arr[x][y]
            arr[x][y] = 0

        print(dice[5])