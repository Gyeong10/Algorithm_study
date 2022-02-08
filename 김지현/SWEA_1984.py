test = int(input())

for t in range(test):
    num = list(map(int, input().split()))
    total = 0
    for n in num:
        if n == max(num) or n == min(num):
            continue
        else:
            total += n
    print(f'#{t+1} {int(round(total/8,0))}')