grid = [[0]*101 for _ in range(101)]

case_num = int(input())
for _ in range(case_num):
    now_i, now_j = map(int, input().split())
    for i in range(now_i, now_i+10):
        for j in range(now_j, now_j+10):
            grid[i][j] += 1

count = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] > 0:
            count += 1

print(count)
