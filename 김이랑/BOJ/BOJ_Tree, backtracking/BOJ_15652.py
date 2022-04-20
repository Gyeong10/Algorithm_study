N, M = map(int, input().split())

answer = []


def dfs(D, start):
    if D == M:
        for i in range(M):
            print(answer[i], end=' ')
        print()
        return
    else:
        for i in range(start, N+1):
            answer.append(i)
            dfs(D+1, i)
            answer.pop()


dfs(0, 1)
