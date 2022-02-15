import sys
sys.stdin = open('sample_input.txt', 'r')

case_num = int(input())
for test_case in range(1, case_num+1):
    today_max, today_win_rate, total_win_rate = map(int, input().split())
    answer = 'Broken'
    #전체 승률이 100인데 오늘 질 수 없지
    if total_win_rate == 100 and today_win_rate != 100:
        pass
    # 전체 승률이 0 인데 오늘 이길순없지
    elif total_win_rate == 0 and today_win_rate != 0:
        pass
    # 오늘 게임한수 곱하면 정수 되어야함
    else:
        for i in range(1, today_max+1):
            if (today_win_rate*i/100) == (today_win_rate*i//100):
                answer = 'Possible'
                break
    print(f"#{test_case} {answer}")



