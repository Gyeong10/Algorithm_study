T = int(input())

for t in range(1, T+1):
    N, pd, pg = map(int, input().split())
    ans = 'Broken'
    if (pg == 0 and pd != 0) or (pg == 100 and pd != 100):
        pass
    else:
        for n in range(1,N+1):
            if (n * pd / 100) == (n * pd // 100):
                ans = 'Possible'
                break

    
    print(f'#{t} {ans}')
