import sys
from collections import deque

sys.stdin = open('BOJ_14888.txt')

def comb(n, k):
    if (n-1) == k:
        cal.append(arr[:])
    else:
        for i in range(4):
            if used[i]:
                arr.append(A[i])
                used[i] -= 1
                comb(n, k + 1)
                used[i] += 1
                arr.pop()


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
used = list(map(int, sys.stdin.readline().split()))

num = deque()

A = [i for i in range(4)]

arr = []
cal = []

comb(N, 0)

ans = set()

for c in cal:
    num = deque()
    for i in range(N):
        num.append(numbers[i])

    for i in range(len(c)):
        a = num.popleft()
        b = num.popleft()
        if c[i] == 0:
            num.appendleft(a + b)
        elif c[i] == 1:
            num.appendleft(a - b)
        elif c[i] == 2:
            num.appendleft(a * b)
        else:
            if a >= 0 and b >= 0:
                num.appendleft(a // b)
            elif a < 0 and b >= 0:
                num.appendleft(-(abs(a) // b))

    ans.add(num[0])
print(max(ans))
print(min(ans))
