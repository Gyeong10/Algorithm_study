# 직사각형 네개의 합집합의 면적 구하기

import sys

arr = [[0]*100 for _ in range(100)]

for i in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for y in range(b, d):
        for x in range(a, c):
            arr[y][x] = 1

cnt = 0
for i in range(100):
    for y in range(100):
        if arr[i][y] == 1:
            cnt += 1

print(cnt)