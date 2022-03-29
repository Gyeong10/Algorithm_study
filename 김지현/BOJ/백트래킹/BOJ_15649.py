import sys

def dfs():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

N, M = map(int, sys.stdin.readline().split())
arr = []
dfs()