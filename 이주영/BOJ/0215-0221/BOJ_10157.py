c, r = map(int, input().split())
t = int(input())
if t > c*r:
    print(0)
elif t <= r:
    print(1, t)
else:
    x = y = value = 1
    k = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    arr = [[0] * (c+1) for _ in range(r+1)]
    for value in range(1, r*c+1):
        arr[y][x] = value
        x = x + dx[k]
        y = y + dy[k]
        if x < 1 or y < 1 or x > c or y > r or arr[y][x]:
            x = x - dx[k]
            y = y - dy[k]
            k = (k+1) % 4
            x = x + dx[k]
            y = y + dy[k]

    for i in range(1, r+1):
        for j in range(1, c+1):
            if arr[i][j] == t:
                print(j, i)