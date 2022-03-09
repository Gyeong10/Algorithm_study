N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
result = []
for n in range(N):
    for m in range(N):
        if arr[n][m] == 1:
            cnt = 1
            Q = []
            Q.append((n,m))
            visited[n][m] = 1
            while Q:
                i, j = Q.pop(0)
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        Q.append((ni,nj))
                        visited[ni][nj] = 1
                        cnt += 1
                        arr[ni][nj] = 0
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)

