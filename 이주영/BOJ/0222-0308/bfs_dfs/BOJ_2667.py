N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
stack = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
houses = []      # 단지별 집 개수

while True:
    flag = 0
    house = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                stack = [(i, j)]
                flag = 1
                break
        if flag:
            break
    else:
        break

    while stack:
        house += 1
        now = stack.pop()
        arr[now[0]][now[1]] = 0
        for k in range(4):
            ni, nj = now[0] + di[k], now[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and (ni, nj) not in stack:
                stack.append((ni, nj))
    houses.append(house)

print(len(houses))
houses.sort()
print(*houses,sep='\n')