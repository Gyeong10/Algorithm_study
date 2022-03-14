# 줄 세우기

import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

order = [0]*N

for i in range(N):
    if order[N - students[i]-1] != 0:
        order = order[:N-students[i]] + [0] + order[N-students[i]:]
        order = order[1:]
        order[N-students[i]-1] = i + 1
    else:
        order[N-students[i]-1] = i + 1

for j in range(N):
    print(order[j], end=' ')