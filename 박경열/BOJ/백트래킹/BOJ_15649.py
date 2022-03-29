import sys

sys.stdin = open('BOJ_15649.txt')

def comb(s, n, r):
    if not r:
        print(*arr)
    else:
        for i in range(N):
            if not used[i]:
                arr[s] = A[i]
                used[i] = 1
                comb(s+1, n, r-1)
                used[i] = 0


N, M = map(int, sys.stdin.readline().split())

arr = [0] * M
used = [0] * N
A = [i for i in range(1, N+1)]
comb(0, N, M)