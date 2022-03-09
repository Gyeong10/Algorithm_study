import sys
from collections import deque
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def BFS():
    day = 0
    while Q:
        day += 1
        for _ in range(len(Q)):
            x,y,z = Q.popleft()
            for l in range(6):
                nx = x + dx[l]
                ny = y + dy[l]
                nz = z + dz[l]
                if 0<=nx<H and 0<=ny<N and 0<=nz<M and arr[nx][ny][nz] == 0:
                    arr[nx][ny][nz] = 1
                    Q.append([nx,ny,nz])

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1
    
    return day -1



M, N, H = map(int, sys.stdin.readline().split())
arr = []
Q = deque()
for i in range(H):
    arr.append([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                Q.append([i,j,k])

print(BFS())