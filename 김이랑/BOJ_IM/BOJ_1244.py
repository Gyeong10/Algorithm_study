switch_num = int(input())
switches = list(map(int, input().split()))

student_num = int(input())
for i in range(student_num):
    stu_sex, stu_location = map(int, input().split())
    # 남자
    if stu_sex == 1:
        count = 1
        while stu_location * count - 1 < switch_num:
            if switches[stu_location * count - 1] == 1:
                switches[stu_location * count - 1] = 0
            else:
                switches[stu_location * count - 1] = 1
            count += 1

    # 여자
    else:
        # 첫자리 변경
        if switches[stu_location - 1] == 1:
            switches[stu_location - 1] = 0
        else:
            switches[stu_location - 1] = 1

        # 앞뒤로 이동하기
        count = 1
        if stu_location-count-1 >= 0 and stu_location+count <= switch_num:
            while switches[stu_location-count-1] == switches[stu_location+count-1]:
                if switches[stu_location-count-1] == 1:
                    switches[stu_location-count-1] = switches[stu_location+count-1] = 0
                else:
                    switches[stu_location-count-1] = switches[stu_location+count-1] = 1
                count += 1
                if stu_location-count-1 < 0 or stu_location+count > switch_num:
                    break

for i in range(switch_num):
    print(switches[i], end=' ')
    if i != 0 and i % 20 == 19:
        print()