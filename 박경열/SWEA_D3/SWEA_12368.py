# D3 24시간

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    print(f'#{tc+1} {(A+B) % 24}')