# 13458 시험 감독
import sys; sys.stdin = open('BOJ_13458.txt')
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(len(A)):
    if 0 < A[i] - B:
        cnt += math.ceil((A[i] - B) / C) + 1
    else:
        cnt += 1

print(cnt)