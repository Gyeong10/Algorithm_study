# D3 교환학생

T = int(input())

for tc in range(T):
    N = int(input())
    week = list(map(int, input().split()))

    ans = [0]*7
    for i in range(7):
        cnt = N
        day = i

        while cnt != 0:
            day = day % 7

            if week[day] == 1:
                cnt -= 1
                ans[i] += 1
                day += 1
            else:
                ans[i] += 1
                day += 1

    real_ans = ans[0]
    for i in range(1, 7):
        if real_ans > ans[i]:
            real_ans = ans[i]

    print(f'#{tc+1} {real_ans}')