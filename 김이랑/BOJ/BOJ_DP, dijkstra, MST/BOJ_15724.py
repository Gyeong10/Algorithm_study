R, C = map(int, input().split())

grid = [[0]*(C+1)]
grid += [[0]+list(map(int, input().split())) for _ in range(R)]
grid += [[0]*(C+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        grid[i][j] = grid[i][j] + grid[i][j-1] + grid[i-1][j] - grid[i-1][j-1]


K = int(input())
for i in range(K):
    s_r, s_c, e_r, e_c = map(int, input().split())
    print(grid[e_r][e_c] - grid[e_r][s_c-1] - grid[s_r-1][e_c] + grid[s_r-1][s_c-1])
