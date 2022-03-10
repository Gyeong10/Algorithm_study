# 종이자르기

import sys

def sort(a):
    r = len(a)
    for i in range(r-1):
        idx = i
        for j in range(i+1, r):
            if a[idx] > a[j]:
                idx = j
        a[i], a[idx] = a[idx], a[i]
    return a


X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

n = [0] # Y
m = [0] # X

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a:
        m.append(b)
    else:
        n.append(b)

n = sort(n) + [Y]
m = sort(m) + [X]

ans = 0
for i in range(1, len(n)):
    for j in range(1, len(m)):
        sqr = (m[j]-m[j-1])*(n[i]-n[i-1])
        if sqr > ans:
            ans = sqr

print(ans)