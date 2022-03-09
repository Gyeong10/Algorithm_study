n, m = map(int, input().split())    
maze = [ list(map(int, input())) for _ in range(n)]


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

Q = [(0,0)]
while Q:
    i, j = Q.pop(0)
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1:
                maze[ni][nj] = maze[i][j] + 1
                Q.append((ni, nj))

print(maze[n - 1][m - 1])