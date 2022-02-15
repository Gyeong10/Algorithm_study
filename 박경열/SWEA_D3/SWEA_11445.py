# D3 무한 사전

T = int(input())

for tc in range(T):
    P = input().rstrip()
    Q = input().rstrip()

    if P + 'a' != Q:
        ans = 'Y'
    else:
        ans = 'N'

    print(f'#{tc+1} {ans}')