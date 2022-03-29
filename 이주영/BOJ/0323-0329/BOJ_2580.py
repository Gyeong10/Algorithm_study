# pypy3로 실행해서 시간초과 해결
import sys

def square(x, y, k):    # 3x3 사각형 안에 있는지 확인
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if k == arr[nx+i][ny+j]:
                return False
    return True

def col(y, k):          # 같은 열에 있는지 확인
    for i in range(9):
        if k == arr[i][y]:
            return False
    return True

def row(x, k):          # 같은 행에 있는지 확인
    for j in range(9):
        if k == arr[x][j]:
            return False
    return True


def DFS(idx):
    if idx == len(blank):
        for line in arr:
            print(*line, sep=' ')
        exit(0)             # 이것 때문에 틀렸었음 return 이랑 exit(0) 구분!

    for k in range(1, 10):  # 숫자 1 ~ 9 중 고르기
        x, y = blank[idx]
        if square(x, y, k) and row(x, k) and col(y, k):
            arr[x][y] = k
            DFS(idx+1)
            arr[x][y] = 0


arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            blank.append([i, j])    # 비어있는 좌표
DFS(0)
