import sys; sys.stdin = open('BOJ_2225.txt')

N, K = map(int, sys.stdin.readline().split())

arr = [1] + [0] * N
for i in range(K-1):
    for j in range(N):
        arr[j + 1] += arr[j]

ans = sum(arr)
print(ans % 10**9)

# 1
# 1 / 1 / 1 / 1 / 1 / 1 / 1 => 7
# 7 / 6 / 5 / 4 / 3 / 2 / 1
# 7 6 5 4 3 2 1 / 6 5 4 3 2 1 / 5 4 3 2 1 / 4 3 2 1 / 3 2 1 / 2 1 / 1
