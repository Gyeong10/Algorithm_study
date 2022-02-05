T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [[1]*j for j in range(1, n+1)]
    for num in range(2, n):
        for i in range(1, num):
            arr[num][i] = arr[num-1][i-1] + arr[num-1][i]
    print(f'#{t}')
    for k in range(n):
        print(*arr[k])
