arr = [list(map(int, input().split())) for _ in range(4)]
area = [[0] * 101 for _ in range(101)]

total = 0
for i in range(4):
    for j in range(arr[i][1], arr[i][3]):
        for k in range(arr[i][0], arr[i][2]):
            if area[j][k] == 0:
                area[j][k] = 1
                total += 1
print(total)
