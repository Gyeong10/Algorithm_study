# 딱지놀이

import sys

N = int(sys.stdin.readline())
for x in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    cnta = [0] * 4
    cntb = [0] * 4

    for i in range(1, len(a)):
        cnta[a[i]-1] += 1
    for i in range(1, len(b)):
        cntb[b[i]-1] += 1

    for i in range(1, 5):
        if cnta[-i] > cntb[-i]:
            ans = 'A'
            break
        elif cnta[-i] < cntb[-i]:
            ans = 'B'
            break
        else:
            ans = 'D'
    print(ans)