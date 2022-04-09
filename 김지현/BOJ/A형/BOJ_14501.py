import sys

def dfs(n, price):
    global maximum
    if n > N:
        return

    if n == N:
        if price > maximum:
            maximum = price
        return

    dfs(n + arr[n][0], price + arr[n][1])
    dfs(n+1, price)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maximum = 0
dfs(0, 0)
print(maximum)