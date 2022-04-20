C, R = map(int, input().split())
grid = [[0]*R for _ in range(C)]

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

check = int(input())


def check_direction(a, b):
    for ii in range(4):
        new_i = a + x[ii]
        new_j = b + y[ii]
        if 0 <= new_i < C and 0 <= new_j < R:
            if grid[new_i][new_j] == 0:
                return x[ii], y[ii]


grid[0][0] = 1
i = j = 0
a = b = 1
num = 2
flag = 0
while num <= R*C:
    di, dj = check_direction(i, j)
    while grid[i + di][j + dj] == 0:
        i = i + di
        j = j + dj
        grid[i][j] = num
        if num == check:
            flag = 1
            a = i + 1
            b = j + 1
            break
        else:
            num += 1
            if 0 <= i + di < C and 0 <= j + dj < R:
                pass
            else:
                break
    if flag:
        break

if check > R*C:
    print(0)
else:
    print(a, b)