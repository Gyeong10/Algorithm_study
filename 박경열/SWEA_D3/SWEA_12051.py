# D3 프리셀 통계

def percent(N, D, G):
    if (D != 100 and G == 100) or (D != 0 and G == 0):
        return 'Broken'
    else:
        for i in range(N):
            if int(D * (N - i) / 100) == (D * (N - i) / 100):
                return 'Possible'
        return 'Broken'


T = int(input())

for tc in range(T):
    N, D, G = map(int, input().split())

    print(f'#{tc + 1} {percent(N, D, G)}')