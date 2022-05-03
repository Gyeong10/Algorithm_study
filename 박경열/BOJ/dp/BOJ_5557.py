import sys; sys.stdin = open('BOJ_5557.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 21 for _ in range(N-1)]

if 0 <= arr[0] + arr[1] < 21:
    dp[1][arr[0] + arr[1]] += 1

if 0 <= arr[0] - arr[1] < 21:
    dp[1][arr[0] - arr[1]] += 1


for i in range(2, N-1):
    for j in range(21):
        if dp[i-1][j]:

            if 0 <= j + arr[i] < 21:
                dp[i][j + arr[i]] += dp[i-1][j]

            if 0 <= j - arr[i] < 21:
                dp[i][j - arr[i]] += dp[i-1][j]

print(dp[N-2][arr[-1]])