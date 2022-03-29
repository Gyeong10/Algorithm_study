import sys

sys.stdin = open('BOJ_15652.txt')

def comb(n, r):
    if not r:
        print(*arr)
    else:
        for i in range(N):
            if not arr or arr[-1] <= A[i]:
                arr.append(A[i])
                comb(n, r - 1)
                arr.pop()


N, M = map(int, sys.stdin.readline().split())

arr = []
used = [0] * N
A = [i for i in range(1, N+1)]
comb(N, M)