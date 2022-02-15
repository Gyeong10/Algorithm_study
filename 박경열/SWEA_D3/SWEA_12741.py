# D3 두 전구

T = int(input())
ans = [0]*T

for tc in range(T):
    light = list(map(int, input().split()))

    if light[1] < light[3]:
        A = light[1]
    else:
        A = light[3]

    if light[0] < light[2]:
        B = light[2]
    else:
        B = light[0]

    if A-B < 0:
        ans[tc] = [tc+1, 0]
    else:
        ans[tc] = [tc+1, A-B]

for i in range(T):
    print(f'#{ans[i][0]} {ans[i][1]}')