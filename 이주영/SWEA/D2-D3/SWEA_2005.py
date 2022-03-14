# 파스칼의 삼각형
T = int(input())
for t in range(1, T+1):
    n = int(input())
    # 1로 가득찬 삼각형 형성
    arr = [[1]*j for j in range(1, n+1)]
    # 3번째 줄(arr[2])부터 왼쪽위, 오른쪽위 값을 더해 값을 입력 
    for num in range(2, n):
        for i in range(1, num):
            arr[num][i] = arr[num-1][i-1] + arr[num-1][i]
    print(f'#{t}')
    for k in range(n):
        print(*arr[k])
