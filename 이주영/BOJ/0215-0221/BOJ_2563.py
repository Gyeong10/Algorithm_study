n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * 100 for _ in range(100)]
for i in range(n):
    for j in range(arr[i][0], arr[i][0] + 10):
        for k in range(arr[i][1], arr[i][1] + 10):
            result[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if result[i][j] == 1:
            cnt += 1
print(cnt)