tests = int(input())

for t in range(tests):
    num = int(input())
    total = 0
    for n in range(1,num+1):
        if n % 2:
            total += n
        else:
            total -= n
    print(f'#{t+1} {total}')