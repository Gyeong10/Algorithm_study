# 1953 탈주범 검거

def bfs():
    queue = [[R, C]]
    visited[R][C] = 1
    while queue:
        t = queue.pop(0)
        if visited[t[0]][t[1]] == L:
            return
        a = str(arr[t[0]][t[1]])
        q = dic[a]
        for i in q:
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] and not visited[nx][ny]:
                    b = str(arr[nx][ny])
                    if i == 0 and b != '3' and b != '4' and b != '7':
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[t[0]][t[1]] + 1
                    if i == 1 and b != '2' and b != '4' and b != '5':
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[t[0]][t[1]] + 1
                    if i == 2 and b != '3'  and b != '5' and b != '6':
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[t[0]][t[1]] + 1
                    if i == 3 and b != '2' and b != '6' and b != '7':
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[t[0]][t[1]] + 1

dic = {
    '1': [0, 1, 2, 3],
    '2': [0, 2],
    '3': [1, 3],
    '4': [0, 1],
    '5': [1, 2],
    '6': [2, 3],
    '7': [0, 3]
}

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    bfs()

    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                ans += 1

    print(f'#{tc + 1} {ans}')