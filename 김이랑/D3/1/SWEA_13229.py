import sys
sys.stdin = open("sample_input.txt", "r")
case_num = int(input())
for test_case in range(1, case_num + 1):
    day = input()
    #이게.. 맞나?
    day_dict = {'SUN' : 7, 'MON' : 6, 'TUE' : 5, 'WED' : 4, 'THU' : 3, 'FRI' : 2, 'SAT' : 1}
    print(f'#{test_case} {day_dict.get(day)}')
