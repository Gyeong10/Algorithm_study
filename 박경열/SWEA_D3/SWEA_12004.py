# D3 구구단 1

T = int(input())

for tc in range(T):
    N = int(input())
    dan = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(1, 10):
        if N / i in dan:
            ans = 'Yes'
            break
        else:
            ans = 'No'

    print(f'#{tc+1} {ans}')