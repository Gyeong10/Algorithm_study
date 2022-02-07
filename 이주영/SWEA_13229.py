T = int(input())
arr = [input() for _ in range(T)]
days = ['', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
for t in range(T):
    for i, day in enumerate(days):
        if day == arr[t]:
            print(f'#{t+1} {i}')