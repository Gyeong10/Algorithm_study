T = int(input())

for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[N-1]
    benefit = 0
    for i in range(N-1, -1, -1):
        if price[i] >= max_price:
            max_price = price[i]
        else:
            benefit += max_price - price[i]
    print(f'#{t} {benefit}')