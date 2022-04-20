# 그리드 생성
grid = [[0]*101 for _ in range(101)]

# 입력받는 평면에 1씩 더하기
for i in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for k in range(b, d):
            grid[j][k] += 1

count = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] > 0:
            count += 1

print(count)