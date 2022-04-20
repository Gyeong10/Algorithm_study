import sys
sys.stdin = open("sample_input.txt", "r")

test_num = int(input())
for test_case in range(1, test_num + 1):
    need_time = int(input())
    schedule = list(map(int, input().split()))

    week_lecture = 0
    lecture_days = []

    for i in range(len(schedule)):
        if schedule[i] == 1:
            week_lecture += 1
            lecture_days.append(i)

    full_week = (need_time // week_lecture) - 1
    rest_lecture = need_time - (full_week * week_lecture)

    min_day = 14

    for i in range(len(schedule)):
        curr_time = 0
        if bool(schedule[i]):
            for j in range(14):
                if schedule[(i+j) % 7] == 1:
                    curr_time += 1
                if curr_time == rest_lecture:
                    if j+1 < min_day:
                        min_day = j+1
                        break

    day = (full_week*7) + min_day

    print(f"#{test_case} {day}")