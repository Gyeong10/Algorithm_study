T = int(input())

for t in range(1, T+1):
    D, L, N = map(int, input().split())

    n = 0
    damage = 0
    for i in range(N):
        damage += D*(1+ (n*L)/100)
        n += 1
    print(f'#{t} {damage:.0f}')