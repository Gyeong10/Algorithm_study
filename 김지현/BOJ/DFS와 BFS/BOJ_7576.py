import sys
from collections import deque
def BFS():
    day = 0
    while Q:
        day += 1 
        for _ in range(len(Q)):
            i, j = Q.popleft()
            
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = i + di 
                nj = j + dj 
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        arr[ni][nj] = 1
                        Q.append((ni,nj))

    for i in range(N):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                return -1
    return day - 1

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque([])

for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            Q.append((i, j))
print(BFS())