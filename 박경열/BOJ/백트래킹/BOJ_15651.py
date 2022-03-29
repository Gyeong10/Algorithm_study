import sys

sys.stdin = open('BOJ_15651.txt')

def comb(n, r):
    if not r:
        print(*arr)
    else:
        for i in range(N):
                arr.append(A[i])
                comb(n, r - 1)
                arr.pop()


N, M = map(int, sys.stdin.readline().split())

arr = []
A = [i for i in range(1, N+1)]
comb(N, M)