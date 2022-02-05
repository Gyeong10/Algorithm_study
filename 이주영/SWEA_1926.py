# 정수 입력
n = int(input())
# 1부터 n까지 숫자 사용
for num in range(1, n+1):
    cnt = 0
    # 숫자에 3 또는 6 또는 9 가 포함되어 있으면
    # 3, 6, 9의 갯수를 cnt에 저장해 cnt만큼 '-'를 출력
    # 없으면 숫자 그대로 출력
    if '3' in str(num) or '6' in str(num) or '9' in str(num):
        cnt += str(num).count('3') + str(num).count('6') + str(num).count('9')
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')