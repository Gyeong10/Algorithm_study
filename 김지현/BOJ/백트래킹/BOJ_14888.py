import sys

def dfs(k, total, plus, minus, multi, divi):
    global mmax, mmin
    if k == N:
        mmax = max(total, mmax)
        mmin = min(total, mmin)
        return

    if plus:
        dfs(k+1, total+arr[k], plus-1, minus, multi, divi)
    if minus:
        dfs(k+1, total-arr[k], plus, minus-1, multi, divi)
    if multi:
        dfs(k+1, total*arr[k], plus, minus, multi-1, divi)
    if divi:
        dfs(k+1, int(total/arr[k]), plus, minus, multi, divi-1)

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
mmax = -1e9
mmin = 1e9
dfs(1, arr[0], oper[0], oper[1], oper[2], oper[3])
print(mmax)
print(mmin)