T = int(input())

for t in range(1, T+1):
    P = input().strip()
    Q = input().strip()
    if Q != P + 'a':
        ans = 'Y'
    else:
        ans = 'N'
    
    print(f'#{t} {ans}')