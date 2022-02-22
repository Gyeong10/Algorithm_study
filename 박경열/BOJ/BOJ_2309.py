# 일곱 난쟁이

import sys

def fun(arr):

    for i in range(1<<9):
        sum, cnt = 0, 0
        short = [0] * 9
        for j in range(9):
            if i & (1<<j):
                sum += arr[j]
                short[j]= arr[j]
                cnt += 1

        if sum == 100 and cnt == 7:
            return short

def my_sort(arr):
    for i in range(8):
        minIdx = i
        for j in range(i+1, 9):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr[2:]


height = [0]*9
for i in range(9):
    height[i] = int(sys.stdin.readline())

arr = fun(height)
ans = my_sort(arr)

for i in range(7):
    print(ans[i])