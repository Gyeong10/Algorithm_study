# 수열

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt_up, cnt_down = 0, 0
ans = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        cnt_up += 1
        cnt_down = 0
    elif arr[i] < arr[i-1]:
        cnt_down += 1
        cnt_up = 0
    else:
        cnt_down += 1
        cnt_up += 1

    if cnt_up > ans:
        ans = cnt_up

    if cnt_down > ans:
        ans = cnt_down


print(ans + 1)