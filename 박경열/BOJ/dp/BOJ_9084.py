import sys; sys.stdin = open('BOJ_9084.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    P = [1] + [0] * M

    for coin in coins:
        for i in range(1, M+1):
            if i - coin >= 0:
                P[i] += P[i-coin]

    print(P[M])