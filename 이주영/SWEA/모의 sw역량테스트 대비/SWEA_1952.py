import sys

sys.stdin = open('1952_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    costs = list(map(int, input().split()))
    schedule = [0] + list(map(int, input().split()))
    cost = [0] * 13
    for i in range(1, 13):
        cost[i] = min(schedule[i] * costs[0], costs[1]) + cost[i-1]
        if i > 2:
            cost[i] = min(cost[i], costs[2]+cost[i-3])
    print(f'#{t} {min(costs[3], cost[12])}')
