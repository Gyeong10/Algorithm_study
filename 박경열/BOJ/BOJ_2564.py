# 경비원

import sys

X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
arr = []
for _ in range(N+1):
    arr.append(list(map(int, sys.stdin.readline().split())))

sum = 0
if arr[N][0] == 1:
    for i in range(N):
        if arr[i][0] == arr[N][0]:
            sum += abs(arr[N][1]-arr[i][1])
        elif arr[i][0] == 3:
            sum += arr[i][1] + arr[N][1]
        elif arr[i][0] == 4:
            sum += arr[i][1] + X - arr[N][1]
        else:
            a = Y + arr[N][1] + arr[i][1]
            b = Y + 2*X - arr[N][1] - arr[i][1]
            if a > b:
                sum += b
            else:
                sum += a

elif arr[N][0] == 2:
    for i in range(N):
        if arr[i][0] == arr[N][0]:
            sum += abs(arr[N][1]-arr[i][1])
        elif arr[i][0] == 3:
            sum += Y - arr[i][1] + arr[N][1]
        elif arr[i][0] == 4:
            sum += Y - arr[i][1] + X - arr[N][1]
        else:
            a = Y + arr[N][1] + arr[i][1]
            b = Y + 2*X - arr[N][1] - arr[i][1]
            if a > b:
                sum += b
            else:
                sum += a

elif arr[N][0] == 3:
    for i in range(N):
        if arr[i][0] == arr[N][0]:
            sum += abs(arr[N][1]-arr[i][1])
        elif arr[i][0] == 1:
            sum += arr[i][1] + arr[N][1]
        elif arr[i][0] == 2:
            sum += arr[i][1] + Y - arr[N][1]
        else:
            a = X + arr[N][1] + arr[i][1]
            b = X + 2*Y - arr[N][1] - arr[i][1]
            if a > b:
                sum += b
            else:
                sum += a

else:
    for i in range(N):
        if arr[i][0] == arr[N][0]:
            sum += abs(arr[N][1]-arr[i][1])
        elif arr[i][0] == 1:
            sum += X - arr[i][1] + arr[N][1]
        elif arr[i][0] == 2:
            sum += X - arr[i][1] + Y - arr[N][1]
        else:
            a = X + arr[N][1] + arr[i][1]
            b = X + 2*Y - arr[N][1] - arr[i][1]
            if a > b:
                sum += b
            else:
                sum += a

print(sum)