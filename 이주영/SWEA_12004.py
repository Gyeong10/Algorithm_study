# N을 a와 b의 곱을 표현할 수 있는지 (1 <= a, b <= 9)
T = int(input())
arr = [int(input()) for _ in range(T)]
for t in range(T):
    # 1~9 로 나누었을 때 그 값이 1이상 9이하의 정수이면 Yes를 출력, 아니면 No를 출력
    for a in range(1, 10):
        if ((arr[t] / a) == (arr[t] // a)) and 1 <= (arr[t] / a) <= 9:
            print(f'#{t+1} Yes')
            break
    else:
        print(f'#{t+1} No')