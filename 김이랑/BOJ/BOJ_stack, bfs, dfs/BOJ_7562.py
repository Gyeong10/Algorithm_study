from collections import deque

for test_case in range(int(input())):
    N = int(input())
    grid = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start_row, start_col = map(int, input().split())
    row, col = map(int, input().split())

    move_row = [-2, -1, 1, 2, 2, 1, -1, -2]
    move_col = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs(now_row, now_col, count):
        global min_num
        queue = deque()
        visited[now_row][now_col] = 1
        queue.append((now_row, now_col, count))
        while queue:
            now_row, now_col, count = queue.popleft()
            if now_row == row and now_col == col:
                if count < min_num:
                    min_num = count
            elif count > min_num:
                pass
            else:
                for i in range(8):
                    next_col = now_col + move_col[i]
                    next_row = now_row + move_row[i]
                    if 0<=next_row<N and 0<=next_col<N and visited[next_row][next_col] == 0:
                        visited[next_row][next_col] = visited[now_row][now_col] + 1
                        queue.append((next_row, next_col, count+1))


    min_num = 90000
    bfs(start_row, start_col, 0)
    print(min_num)