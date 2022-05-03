for tc in range(int(input())):
    N = int(input())
    input_moneys = list(map(int, input().split()))
    M = int(input())
    moneys = [0]*(M+1)
    moneys[0] = 1

    for input_money in input_moneys:
        for i in range(1, M+1):
            if i >= input_money:
                moneys[i] += moneys[i-input_money]

    print(moneys[-1])