# 가장 먼 일요일 찾기
T = int(input())
arr = [input() for _ in range(T)]
# 요일 리스트 선언, index값을 일요일과의 차이로 사용
days = ['', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
for t in range(T):
    # day의 값과 arr[t]의 값이 같을 때 그 days의 index값을 출력
    for i, day in enumerate(days):
        if day == arr[t]:
            print(f'#{t+1} {i}')