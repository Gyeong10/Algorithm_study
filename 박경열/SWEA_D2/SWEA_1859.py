# D2 백만 장자 프로젝트

T = int(input())

for i in range(T):
    N = int(input())
    sell = list(map(int, input().split()))
    a = sell[-1]
    ans = 0

    for j in range(2, N+1):
        if a > sell[-j]:
            ans += abs(a - sell[-j])
        else:
            a = sell[-j]

    print(f'#{i+1} {ans}')