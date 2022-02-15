# D3 구구단2

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    if A >= 10 or B >= 10:
        ans = -1
    else:
        ans = A*B

    print(f'#{tc+1} {ans}')