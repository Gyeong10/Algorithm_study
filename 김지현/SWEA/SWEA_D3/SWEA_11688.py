T = int(input())

for t in range(1, T+1):
    tree = list(input())
    result = [1,1]

    for i in tree:
        if i == 'L':
            result [1] = result[0] + result[1]
        else:
            result[0] = result[0] + result[1]

    print(f'#{t}', end=' ')
    print(*result)