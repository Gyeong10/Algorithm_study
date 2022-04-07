N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
# 0, 동, 서, 남, 북, 반대의 값을 넣을거임
dice = [0, 0, 0, 0, 0, 0]
pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]

order = list(map(int, input().split()))
for i in range(K):
    new_dice = []
    if 0 <= x + pos[order[i]-1][0] < N and 0 <= y + pos[order[i]-1][1] < M:
        x, y = x + pos[order[i]-1][0], y + pos[order[i]-1][1]
        if grid[x][y] == 0:
            grid[x][y] = dice[order[i]]
        else:
            dice[order[i]] = grid[x][y]
            grid[x][y] = 0

        if order[i] == 1:
            new_dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
        elif order[i] == 2:
            new_dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
        elif order[i] == 3:
            new_dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
        elif order[i] == 4:
            new_dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
        dice = new_dice
        print(dice[5])