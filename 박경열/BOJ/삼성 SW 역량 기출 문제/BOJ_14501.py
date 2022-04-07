# 14501 퇴사
import sys; sys.stdin = open('BOJ_14501.txt')

def solve(k, ssum):
    global ans

    if k > N:
        return

    if k == N:
        if ans < ssum:
            ans = ssum
        return

    solve(k + arr[k][0], ssum + arr[k][1])
    solve(k + 1, ssum)


N = int(input())
arr = [0] * N
for i in range(N):
    d, m = map(int, sys.stdin.readline().split())
    arr[i] = [d, m]
ans = 0
solve(0, 0)
print(ans)