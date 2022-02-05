T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for startx in range(n-m+1):
        for starty in range(n-m+1):
            total = 0
            for i in range(startx, startx + m):
                total += sum(arr[i][starty:starty+m])
            result = total if total > result else result
    print(f'#{t} {result}')