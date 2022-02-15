# D3 오목 판정

def baduk(N, arr):
    a = ['o', 'o', 'o', 'o', 'o']
    rra = list(map(list, zip(*arr)))

    for i in range(N):
        for j in range(N-4):
            if arr[i][j:j+5] == a or rra[i][j:j+5] == a:
                return 'YES'

    for i in range(N-4):
        for k in range(N-4):
            li = [arr[i][k:k+5],arr[i+1][k:k+5],arr[i+2][k:k+5],arr[i+3][k:k+5],arr[i+4][k:k+5]]

            oi1 = [li[0][0],li[1][1],li[2][2],li[3][3],li[4][4]]
            oi2 = [li[0][4],li[1][3],li[2][2],li[3][1],li[4][0]]
            if oi1 == a or oi2 == a:
                return 'YES'

    return 'NO'


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = baduk(N, arr)
    print(f'#{tc+1} {ans}')



#
def baduk(N, arr):
    a = ['o', 'o', 'o', 'o', 'o']
    rra = list(map(list, zip(*arr)))

    for i in range(N):
        for j in range(N-4):
            if arr[i][j:j+5] == a or rra[i][j:j+5] == a:
                return 'YES'

    for i in range(N-4):
        for k in range(N-4):
            li = [arr[i][k:k+5],arr[i+1][k:k+5],arr[i+2][k:k+5],arr[i+3][k:k+5],arr[i+4][k:k+5]]

            oi1 = ['']*5
            oi2 = ['']*5
            for j in range(5):
                oi1[j] = li[j][j]
                oi2[j] = li[j][4-j]

            if oi1 == a or oi2 == a:
                return 'YES'

    return 'NO'


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = baduk(N, arr)
    print(f'#{tc+1} {ans}')