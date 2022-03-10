from collections import deque
import sys
pos_i = [0, 0, 1, -1]
pos_j = [1, -1, 0, 0]


for test_case in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for i in range(K):
        s, e = map(int, sys.stdin.readline().split())
        grid[e][s] = 1

    def bfs(i, j):
        global count
        count += 1
        queue = deque()
        queue.append([i, j])

        while queue:
            now = queue.popleft()
            now_i = now[0]
            now_j = now[1]
            visited[now_i][now_j] = 1

            for i in range(4):
                next_i = now_i + pos_i[i]
                next_j = now_j + pos_j[i]

                if 0<=next_i<N and 0<=next_j<M:
                    if grid[next_i][next_j] == 1 and visited[next_i][next_j] == 0:
                        visited[next_i][next_j] = 1
                        queue.append([next_i, next_j])


    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)

    print(count)