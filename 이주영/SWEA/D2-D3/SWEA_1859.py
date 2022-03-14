# 백만장자(최대이익, 하루에 1개만 살 수 있음)
# 테스트 케이스 수 입력
T = int(input())
for t in range(1, T+1):
    # 가격 개수 입력
    n = int(input())
    # 가격 입력
    costs = list(map(int, input().split()))
    # 최대값을 제일 마지막날 값으로 할당
    max_value = costs[-1]
    result = 0
    # 뒤에서부터 매매가를 최대값과 비교하며
    # 최대값보다 그날의 매매가가 더 작은 경우: 최대값에서 매매가를 뺀 이익을 result에 더해줌
    # 최대값보다 그날의 매매가가 더 크거나 같은 경우: 최대값을 그날의 매매가로 변경
    for cost in costs[::-1]:
        if max_value > cost:
            result += max_value - cost
        else:
            max_value = cost
    print(f'#{t} {result}')
