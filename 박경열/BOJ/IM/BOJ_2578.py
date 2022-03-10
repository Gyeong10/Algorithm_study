# 빙고

import sys

def search(n, m):
    for x in range(5):
        for y in range(5):
            if n[i][j] == m[x][y]:
                m[x][y] = 0
                return

def end(m):
    c = 0
    flag = 1

    for i in range(5):
        if m[i] == [0]*5:
            c += 1

    for i in range(5):
        x = 0
        for j in range(5):
            x += m[j][i]
        if x == 0:
            c += 1

    a, b = 0, 0
    for i in range(5):
        a += m[i][i]
    if a == 0:
        c += 1

    for i in range(5):
        b += m[i][4-i]
    if b == 0:
        c += 1

    if c >= 3:
        flag = 0
        return flag

    return flag


bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
cnt = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

count = 0
flag = 1
for i in range(5):
    for j in range(5):
        if flag == 0:
            break

        count += 1
        search(cnt, bingo)
        flag = end(bingo)

print(count)