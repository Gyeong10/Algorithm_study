from collections import deque

N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answers = []
pos_i = [0, 0, 1, -1]
pos_j = [1, -1, 0, 0]

def bfs(ii, jj):
    queue = deque()
    queue.append([ii, jj])
    count = 0
    while queue:
        now = queue.popleft()
        count += 1
        now_i = now[0]
        now_j = now[1]
        visited[now_i][now_j] = 1
        for i in range(4):
            next_i = now_i + pos_i[i]
            next_j = now_j + pos_j[i]
            if 0<=next_i<N and 0<=next_j<N:
                if grid[next_i][next_j] == 1 and visited[next_i][next_j] == 0:
                    visited[next_i][next_j] = 1
                    queue.append([next_i, next_j])
    answers.append(count)

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

answers.sort()

print(len(answers))
for answer in answers:
    print(answer)