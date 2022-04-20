case_num = int(input())
for test_case in range(1, case_num+1):
    roads = input()
    num = [1, 1]
    for road in roads:
        if road == 'L':
            num[1] = num[0] + num[1]
        if road == 'R':
            num[0] = num[0] + num[1]
 
    print(f"#{test_case} {num[0]} {num[1]}")