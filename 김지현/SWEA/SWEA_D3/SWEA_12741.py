T = int(input())
result = []
for t in range(T):
    s1, e1, s2, e2 = map(int, input().split())
    
    ans = 0
    for i in range(s1,e1):
        if s2 <= i <e2:
            ans += 1
    
    result.append(f'#{t+1} {ans}')

print(*result, sep='\n')
