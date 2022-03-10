T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    up = down = 1
    if arr[t][0] == 1:
        up = arr[t][1]
    elif arr[t][0] != arr[t][1]:
        for i in range(arr[t][1], arr[t][1] - arr[t][0], -1):
            up *= i
        for i in range(arr[t][0], 0, -1):
            down *= i
    print(up//down)