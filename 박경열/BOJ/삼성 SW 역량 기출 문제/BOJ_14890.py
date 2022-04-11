# 14890 경사로

import sys; sys.stdin = open('BOJ_14890.txt')

def solve():
    used = [0] * N
    j = 0

    while j < N - 1:

        if arr[i][j] == arr[i][j + 1]:
            j += 1
        elif abs(arr[i][j] - arr[i][j + 1]) == 1:
            if arr[i][j] > arr[i][j + 1]:
                comp = arr[i][j + 1]
                for x in range(1, L+1):
                    if j + x >= N or comp != arr[i][j+x] or used[j+x]:
                        return 0
                    else:
                        used[j+x] = 1
                j += L
            elif arr[i][j] < arr[i][j+1]:
                comp = arr[i][j]
                for x in range(L):
                    if j - x < 0 or comp != arr[i][j-x] or used[j-x]:
                        return 0
                    else:
                        used[j-x] = 1
                j += 1
        else:
            return 0
    return 1


N, L = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    cnt += solve()

arr = list(zip(*arr))
for i in range(N):
    cnt += solve()

print(cnt)