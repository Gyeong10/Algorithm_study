import sys
sys.stdin = open('sample_input.txt', 'r')

case_num = int(input())
for test_case in range(1, case_num+1):
    num = int(input())
    answer = 'No'
    for i in range(1, 10):
        for j in range(1,10):
            if num == i*j:
                answer = 'Yes'
                break

    print(f"#{test_case} {answer}")



