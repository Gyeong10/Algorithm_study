N, M = map(int, input().split())
check = [False]*N
answer = [0]*M


def dfs(D):
    if D == M:
        for i in range(M):
            print(answer[i], end=' ')
        print()
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        answer[D] = i+1
        dfs(D+1)
        check[i] = False


dfs(0)