import sys
sys.stdin = open("input (1).txt", "r")

test_num = int(input())

# 걍 뒤에서 보자 근데 왜 인덱스는 안되지ㅠㅠㅠ?
for i in range(1, test_num + 1):
    case_list_len = int(input())
    case_list = list(map(int, input().split()))
    case_list.reverse()

    answer = 0
    max = case_list[0]
    for reverse_case in case_list:
        if max > reverse_case:
            answer = answer + max - reverse_case
        else:
            max = reverse_case

    print(f'#{i} {answer}')




