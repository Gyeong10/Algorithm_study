# 반복되는 문자열 길이 출력
T = int(input())
for t in range(1, T+1):
    long_str = input()
    # 반복 문자열이 최대 10글자이기 때문에 10까지만 확인
    for i in range(1, 11):
        # 문자열의 i(index)를 기준으로 같은 길이로 분할했을 때 같으면 그 index 출력
        if long_str[:i] == long_str[i:2*i]:
            print(f'#{t} {i}')
            break