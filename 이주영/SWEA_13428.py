# 숫자를 최대 한쌍 바꿔 만들 수 있는 수의 최대값, 최솟값 구하기
T = int(input())
arr = [list(input()) for _ in range(T)]
for t in range(T):
    # 최댓값, 최솟값을 처음 숫자로 초기화
    max_value = int(''.join(arr[t]))
    min_value = int(''.join(arr[t]))
    # 첫번째 index부터 마지막 바로 앞 index까지 사용
    for x in range(len(arr[t])-1):
        # x보다 큰 index값부터 마지막 index까지 사용
        for y in range(x+1, len(arr[t])):
            # 바꾸려는 쌍이 첫번째자리의 숫자와 0인 경우 코드실행하지 않고 다시 반복문 수행
            if arr[t][y] == '0' and x == 0:
                continue
            # 수를 교환해 change변수에 할당한 후
            # max_value보다 change가 크면 change값을 할당하고 아니면 그대로
            # min_Value보다 change가 작으면 change값을 할당하고 아니면 그대로
            arr[t][x], arr[t][y] = arr[t][y], arr[t][x]
            change = int(''.join(arr[t]))
            max_value = change if max_value < change else max_value
            min_value = change if min_value > change else min_value
            # 숫자 원래대로 돌리기
            arr[t][x], arr[t][y] = arr[t][y], arr[t][x]
    print(f'#{t+1} {min_value} {max_value}')

