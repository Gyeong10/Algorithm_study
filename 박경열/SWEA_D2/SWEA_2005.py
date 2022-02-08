# D2 파스칼의 삼각형

T = int(input())

for i in range(T):
    tri = [1] + [0] * 10
    N = int(input())

    print(f'#{i+1}')

    for j in range(1, N+1):
        a = tri
        tri = [1] + [0] * 10
        for k in range(1, j+1):
            tri[k] = a[k-1]+a[k]

        for m in range(j):
            print(a[m], end=' ')
        print('')