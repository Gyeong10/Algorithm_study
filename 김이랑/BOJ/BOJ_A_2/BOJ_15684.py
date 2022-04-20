N, M, H = map(int, input().split())

grid = [[0]*(N-1) for _ in range(H)]

for i in range(M):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1


def check():
    global answer
    add = []
    for i in range(N-1):
        temp = 0
        for j in range(H):
            if grid[j][i] == 1:
                temp += 1
        if temp % 2:
            add.append(i)

    if len(add) > 3:
        return

    answer = len(add)


answer = -1
check()

print(answer)