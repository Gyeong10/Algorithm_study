T = int(input())
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for t in range(1, T+1):
    day = list(map(int, input().split()))
    ans = 0

    if day[0] == day[2]:
            ans = day[3] - day[1] + 1
    else:
        for i in range(1,13):
            if i > day[0] and i < day[2]:
                ans += month[i]
        ans += month[day[0]] - day[1] + 1 
        ans += day[3]

    print(f'#{t} {ans}')