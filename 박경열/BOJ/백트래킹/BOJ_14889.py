import sys

sys.stdin = open('BOJ_14889.txt')

def dfs(n, a, b):
    global ans
    if n == N:
        if len(a) == N // 2:
            asum = bsum = 0
            for i in range(N // 2):
                for j in range(N // 2):
                    asum += arr[a[i]][a[j]]
                    bsum += arr[b[i]][b[j]]

            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    dfs(n+1, a + [n], b)
    dfs(n+1, a, b + [n])

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 1000
dfs(0, [], [])
print(ans)