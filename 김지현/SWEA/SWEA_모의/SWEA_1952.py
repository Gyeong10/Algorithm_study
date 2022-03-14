
T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    m = [0] + list(map(int, input().split()))
    cost = [0] * 13

    for i in range(1, 13):
        cost[i] = min(m[i]*price[0], price[1]) + cost[i-1]
        if i > 2:
            cost[i] = min(cost[i], price[2]+cost[i-3])

    print(f'#{tc} {min(cost[12],price[3])}')



