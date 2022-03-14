test = int(input())
day = ['SAT','FRI','THU','WED','TUE','MON','SUN']

for t in range(1,test+1):
    s = input()

    for d in range(len(day)):
        if s == day[d]:
            print(f'#{t} {d+1}')