import sys; sys.stdin = open('BOJ_17144.txt')
from collections import deque

def cleanUp(x, y, k):
    # 경로에 있는 먼지 저장
    dusts = deque()
    # 경로 좌표 저장
    path = deque()

    # 우 상 좌 하 / 우 하 좌 상
    ddx = [[0, -1, 0, 1], [0, 1, 0, -1]]
    ddy = [[1, 0, -1, 0], [1, 0, -1, 0]]

    i = 0
    while True:
        nx = x + ddx[k][i]
        ny = y + ddy[k][i]

        if 0 <= nx < R and 0 <= ny < C:

            if arr[nx][ny] == -1:
                break
            else:
                dusts.append(arr[nx][ny])
                path.append([nx, ny])
                x, y = nx, ny
        else:
            i = (i + 1) % 4

    # 마지막 먼지 없애고 첫 번째에 먼지 없게
    dusts.pop()
    dusts.appendleft(0)
    while path:
        a, b = path.pop()
        d = dusts.pop()
        arr[a][b] = d


R, C, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dust = deque()

for _ in range(T):
    temp = [[0] * C for _ in range(R)]
    cleaner = []

    # 미세먼지 / 공기청정기 위치 저장
    for i in range(R):
        for j in range(C):
            if 0 < arr[i][j]:
                dust.append([i, j])

            if arr[i][j] == -1:
                cleaner.append([i, j])

    # 1. 미세먼지 확산 - temp에 저장
    while dust:
        x, y = dust.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                temp[nx][ny] += arr[x][y] // 5
                cnt += 1
        arr[x][y] -= (arr[x][y] // 5) * cnt

    # 미세먼지 저장(arr)
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]

    # 2. 공기청정기 작동
    cleanUp(cleaner[0][0], cleaner[0][1], 0)
    cleanUp(cleaner[1][0], cleaner[1][1], 1)

# 결과
ans = 2
for i in range(R):
    ans += sum(arr[i])
print(ans)