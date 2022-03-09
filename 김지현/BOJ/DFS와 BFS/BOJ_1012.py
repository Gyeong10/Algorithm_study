T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for k in range(K):
        i, j = map(int,input().split())
        arr[j][i] = 1
    
    cnt = 0
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 1:
                visited[n][m] = 1
                cnt += 1
                arr[n][m] = 0
                Q = []
                Q.append((n,m))
                while Q:
                    i, j = Q.pop(0)
                    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni, nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                            Q.append((ni,nj))
                            arr[ni][nj] = 0
                            visited[ni][nj] = 1
    print(cnt)