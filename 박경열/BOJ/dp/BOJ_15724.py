import sys; sys.stdin = open('BOJ_15724.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, M):
        arr[i][j] += arr[i][j-1]

K = int(sys.stdin.readline())
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    ans = 0
    for i in range(x1-1, x2):
        ans += arr[i][y2-1]

        if y1 != 1:
            ans -= arr[i][y1-2]

    print(ans)