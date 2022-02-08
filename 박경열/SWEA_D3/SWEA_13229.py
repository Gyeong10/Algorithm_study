# D3 일요일

T = int(input())

week = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']

for i in range(T):
    S = input()
    if S in week:
        print(f'#{i+1} {week.index(S)+1}')