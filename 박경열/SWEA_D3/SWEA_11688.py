# D3 Calkin-Wilf tree 1

T = int(input())

for tc in range(T):
    M = list(input())

    a = 1
    b = 1

    for s in M:
        if s == 'L':
            b += a
        else:
            a += b

    print(f'#{tc+1} {a} {b}')