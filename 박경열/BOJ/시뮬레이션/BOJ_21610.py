import sys; sys.stdin = open('BOJ_21610.txt')
from collections import deque

def checkNum(v):
    global N

    if v < 0:
        v = (N-(-v % N)) % N
    elif v >= N:
        v %= N
    return v


def checkWater(x, y):
    cnt = 0
    for i in water:
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny]:
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

first_cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
cloud = deque()
for cl in first_cloud:
    cloud.append(cl)
# 8방향
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# 물복사버그
water = [2, 4, 6, 8]

for _ in range(M):
    visited = [[0] * N for _ in range(N)]
    d, s = map(int, sys.stdin.readline().split())

    # 1. 모든 구름이 d 방향으로 s 칸 이동
    for c in cloud:
        c[0] += dx[d] * s
        c[1] += dy[d] * s
        c[0] = checkNum(c[0])
        c[1] = checkNum(c[1])
        # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
        arr[c[0]][c[1]] += 1

    # 3. 구름이 모두 사라짐
    # 4. 물복사버그
    while cloud:
        x, y = cloud.popleft()
        arr[x][y] += checkWater(x, y)
        visited[x][y] = 1

    # 5. 새로운 구름
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                cloud.append([i, j])

ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)
