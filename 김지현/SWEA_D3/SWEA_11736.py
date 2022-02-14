T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    
    for i in range(2, N):
        max_value = 0
        min_value = N
        for j in range(-2,1):
            if numbers[i+j] > max_value:
                max_value = numbers[i+j]
            if numbers[i+j] < min_value:
                min_value = numbers[i+j]
            
        if numbers[i-1] != min_value and numbers[i-1] != max_value:
            ans += 1
    print(f'#{t} {ans}')