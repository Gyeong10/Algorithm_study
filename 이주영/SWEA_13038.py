# 교환학생 최소 기간 구하기
T = int(input())
for t in range(1, T+1):
    n = int(input())
    days = list(map(int, input().split()))
    # 값이 1인 index 찾아 바로 다음 index(만약 마지막 index라면 처음으로 돌아가 0)를 list에 담기
    indexs_1 = []
    for i, day in enumerate(days):
        if day == 1:
            if i == 6:
                indexs_1.append(0)
            else:
                indexs_1.append(i + 1)
    # index_1 리스트에 담긴 index로 시작일을 다르게 하여 걸리는 기간 구하기
    min_days = []
    for idx in indexs_1:
        # 시작일을 찾아 그다음부터 반복문을 돌리기 때문에
        # cnt와 min_day를 모두 1로 초기화해준다.
        cnt = 1
        min_day = 1
        # n만큼 들어야 하므로 n과 같아지면 반복문 멈춤
        while cnt < n:
            # 만약 index(idx)가 7 즉, 요일 리스트의 길이를 넘어서면 다시 처음으로 돌아가 0으로 설정 
            if idx == 7:
                idx = 0
            # 1이면 cnt 하나 더해줌
            if days[idx] == 1:
                cnt += 1
            # 반복문 돌 때마다 index(idx) 와 min_day를 1씩 더해줌
            idx += 1
            min_day += 1
        # 반복문이 끝나면 min_days 리스트에 append해줌
        min_days.append(min_day)
    # min_days중 가장 작은 값 출력
    print(f'#{t} {min(min_days)}')