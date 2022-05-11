import sys; sys.stdin = open('BOJ_20056.txt')
from collections import deque

def checkNum(v):
    global N

    if v < 0:
        v = (N-(-v % N)) % N
    elif v >= N:
        v %= N
    return v


N, M, K = map(int, sys.stdin.readline().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 초기 파이어볼 입력 받음
fireball = deque()
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append([r-1, c-1, m, s, d])

for _ in range(K):
    visited = [[0] * N for _ in range(N)]
    # 질량, 속력, 갯수, 방향 합 저장
    marr = [[0] * N for _ in range(N)]
    sarr = [[0] * N for _ in range(N)]
    carr = [[0] * N for _ in range(N)]
    darr = [[0] * N for _ in range(N)]
    # 방향 저장
    darr2 = [[0] * N for _ in range(N)]
    temp = deque()

    l = len(fireball)
    # 1. 모든 파이어볼 날리기
    for i in range(l):
        r, c, m, s, d = fireball.popleft()

        r += dx[d] * s
        c += dy[d] * s

        r = checkNum(r)
        c = checkNum(c)

        carr[r][c] += 1
        marr[r][c] += m
        sarr[r][c] += s
        # 방향에 % 2를 해서 더함 (짝수 => +0) (홀수 => +1)
        darr[r][c] += d % 2
        darr2[r][c] = d

        # 2. 2개 이상 있는 파이어볼 좌표 temp에 저장
        if carr[r][c] == 2 and not visited[r][c]:
            temp.append([r, c])
            visited[r][c] = 1

    # 1개 있는 파이어볼 저장
    for i in range(N):
        for j in range(N):
            if carr[i][j] == 1:
                fireball.append([i, j, marr[i][j], sarr[i][j], darr2[i][j]])

    # 2개 이상 파이어볼 계산
    while temp:
        r, c = temp.popleft()
        # 2.3.1. 질량 = 질량 합 // 5
        m_new = marr[r][c] // 5
        # 새로운 질량이 0이 아닌 경우
        if m_new:
            # 2.3.2. 속력 = 속력 합 / 갯수
            s_new = sarr[r][c] // carr[r][c]
            # 2.3.3. 나눠지는 파이어볼 방향
            # 0일 경우 => 짝수 / 갯수와 값이 같을 경우 => 홀수
            if not darr[r][c] or darr[r][c] == carr[r][c]:
                d_new = [0, 2, 4, 6]
            else:
                d_new = [1, 3, 5, 7]
                # 2.2. 파이어볼 4방향 나누어서 저장
            for i in d_new:
                fireball.append([r, c, m_new, s_new, i])

# 실제 파이어볼이 저장되어 있는 fireball deque에서 파이어볼 질량 계산
ans = 0
for i in range(len(fireball)):
    ans += fireball[i][2]
print(ans)