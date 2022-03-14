T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        baechu = list(map(int, input().split()))
        arr[baechu[1]][baechu[0]] = 1
    cnt = 0
    stack = []
    while True:
        flag = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    stack.append((i, j))
                    cnt += 1
                    flag = 1
                    break
            if flag:
                break
        else:
            break

        while stack:
            now = stack.pop()
            arr[now[0]][now[1]] = 0
            for k in range(4):
                ni, nj = now[0] + di[k], now[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and (ni, nj) not in stack:
                    stack.append((ni, nj))

    print(cnt)