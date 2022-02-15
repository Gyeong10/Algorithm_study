T = int(input())

for t in range(1, T+1):
    N = int(input())
    week = list(map(int, input().split()))

    #처음 수업이 있는 날 찾기
    for i in range(7):
        if week[i] == 1:
            idx = i
            break
    
    ans = 0
    # N이 0될 때까지 돌림
    while N != 0:
        for i in range(7): 
            if N == 0:
                break
            else:
                # 수업있는 날이면 N-1
                if week[i] == 1:
                    N -= 1
            #하루 지날때 ans + 1        
            ans += 1
    
    print(f'#{t} {ans - idx}')