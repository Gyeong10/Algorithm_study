# 15685 드래곤 커브

import sys; sys.stdin = open('BOJ_15685.txt')

def dragon():
    # stack - 방향 저장
    stack = [d]
    # point - 좌표 저장
    point = [[x+dx[d], y+dy[d]]]
    for _ in range(g):
        l = len(stack) - 1
        for j in range(l, -1, -1):
            nd = (stack[j] + 1) % 4
            point.append([point[-1][0] + dx[nd], point[-1][1] + dy[nd]])
            stack.append(nd)
    return point


N = int(sys.stdin.readline())
arr = [[0] * 101 for _ in range(101)]
visited = [[0] * 101 for _ in range(101)]
# 우 상 좌 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for i in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    pnt = dragon()
    # 초기값 x, y 넣음
    arr[x][y] = 1
    for v, w in pnt:
        if 0 <= v < 101 and 0 <= w < 101:
            arr[v][w] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        # arr[i][j]가 1 일때
        if arr[i][j] and i + 1 < 101 and j + 1 < 101:
            # 네모(4개합)이 4
            if arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] == 4:
                # 네모 모두 방문하지 않았을 때
                if visited[i][j] + visited[i][j+1] + visited[i+1][j] + visited[i+1][j+1] != 4:
                    visited[i][j] = visited[i][j+1] = visited[i+1][j] = visited[i+1][j+1] = 1
                    cnt += 1

print(cnt)