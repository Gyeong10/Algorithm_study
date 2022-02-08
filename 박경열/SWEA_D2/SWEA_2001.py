# D2 파리 퇴치

T = int(input())

for a in range(T):
    n, m = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(n)]

    ans = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            al = 0
            for k in range(i, m + i):
                al += sum(fly[k][j: j + m])
            ans.append(al)

    print(f'#{a+1} {max(ans)}')