# D3 평범한 숫자

T = int(input())

for tc in range(T):
    N = int(input())
    M = list(map(int, input().split()))

    cnt = 0
    for i in range(N-2):
        arr = sorted(M[i:i+3])
        if arr[1] == M[i+1]:
            cnt += 1

    print(f'#{tc+1} {cnt}')