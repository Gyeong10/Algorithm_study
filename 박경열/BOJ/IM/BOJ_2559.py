# 수열

import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

list_sum = [0]
temp = 0
for i in range(N):
    temp += arr[i]
    list_sum.append(temp)

ans = []
for i in range(N - K + 1):
    ans.append(list_sum[K+i] - list_sum[i])

print(max(ans))