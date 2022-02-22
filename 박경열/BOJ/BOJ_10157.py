# 자리배정

import sys

def solve(arr, K):
    if K > X*Y:
        return 0

    cnt = 0
    i, j = 0, Y - 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 0
    number = 0
    while True:

        if 0 <= i < X and 0 <= j < Y:
            cnt += 1
            arr[j][i] = cnt

        if K == cnt:
            ans = [1 + i, Y - j]
            return ans

        if 0 <= i+dx[number] < X and 0 <= j+dy[number] < Y and arr[j+dy[number]][i+dx[number]] == 0:
            i += dx[number]
            j += dy[number]
        else:
            num += 1
            number = num % 4
            i += dx[number]
            j += dy[number]


X, Y = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

arr = [[0] * X for _ in range(Y)]
ans = solve(arr, K)

if not ans:
    print(ans)
else:
    for i in range(2):
        print(ans[i], end=' ')