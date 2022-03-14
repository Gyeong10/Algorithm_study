import sys


sys.stdin = open('1949_input.txt', 'r')


def dfs(x, y, cnt=0):       # 최댓값 인덱스 x, y ; cnt : dfs 호출 횟수(등산 거리)
    global max_cnt, flag
    for k in range(4):
        ni, nj = x + di[k], y + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[x][y] > arr[ni][nj] - (K * flag) and not visited[ni][nj]:
            if arr[x][y] <= arr[ni][nj]:    # 한 곳 파기 사용
                flag = 0
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[x][y] - 1
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1)
                visited[ni][nj] = 0
                arr[ni][nj] = tmp
                flag = 1

            else:                           # 한 곳 파기 사용 안함
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1)
                visited[ni][nj] = 0

    val = cnt + 1   # 출발지 더해주기
    if max_cnt < val:
        max_cnt = val


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_index = []  # 최고 높이인 곳 인데스 리스트
    max_value = 0   # 최고 높이
    max_cnt = 0     # 최대 등산로 길이
    flag = 1        # 한곳 파기 사용 가능 여부 (1: Yes, 0: No)
    visited = [[0] * N for _ in range(N)]
    # 최댓값 구하기
    for row in arr:
        if max_value < max(row):
            max_value = max(row)
    # 최댓값을 가진 인덱스 리스트 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_value:
                max_index.append([i, j])
    # 최댓값을 가진 인덱스마다 dfs 수행하기
    for idx in max_index:
        visited[idx[0]][idx[1]] = 1
        dfs(idx[0], idx[1])
        visited[idx[0]][idx[1]] = 0

    print(f'#{t} {max_cnt}')