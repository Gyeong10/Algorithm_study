import sys

def dfs(s):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(s, N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

N, M = map(int, sys.stdin.readline().split())
arr = []
dfs(1)