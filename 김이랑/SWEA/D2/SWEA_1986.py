# 이 문제는 굳이 풀이할 필요가 있을까
test_num = int(input())
for case_num in range(1, test_num + 1):
    num = int(input())
    answer = 0
    for i in range(1, num+1):
        if i % 2 == 1:
            answer = answer + i
        else:
            answer = answer - i

    print(f'#{case_num} {answer}')