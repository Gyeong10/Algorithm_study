# D3 몬스터 사냥

T = int(input())

for tc in range(T):
    D, L, N = map(int, input().split())
    ans = 0

    for i in range(N):
        ans += D*(1+i*L*(1/100))

    print(f'#{tc+1} {int(ans)}')


#
T = int(input())

for tc in range(T):
    D, L, N = map(int, input().split())

    ans = D*N + (((N-1)*N)/2)*D*L*(1/100)

    print(f'#{tc+1} {int(ans)}')