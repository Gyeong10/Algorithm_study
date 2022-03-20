n = int(input())
lights = [0] + list(map(int, input().split()))
p = int(input())
stds = [list(map(int, input().split())) for _ in range(p)]
for i in range(p):
    change = stds[i][1]
    if stds[i][0] == 1:
        for j in range(1, n//change+1):
            if lights[change*j] == 1:
                lights[change*j] = 0
            else:
                lights[change*j] = 1
    elif stds[i][0] == 2:
        change = stds[i][1]
        if lights[change] == 1:
            lights[change] = 0
        else:
            lights[change] = 1
        k = 1
        while change + k <= n and change - k >= 1:
            if lights[change-k] != lights[change+k]:
                break
            if lights[change-k] == 1:
                lights[change-k] = 0
            else:
                lights[change-k] = 1

            if lights[change+k] == 1:
                lights[change+k] = 0
            else:
                lights[change+k] = 1
            k += 1
i = 0
while i < n:
    i += 1
    print(lights[i], end=' ')
    if i % 20 == 0:
        print()
