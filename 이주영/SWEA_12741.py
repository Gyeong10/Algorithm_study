# 두 전구 겹치는 구간 구하기
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    # 두 전구의 켜지는 시간 중 늦은 시간을 x에 담기
    # 두 전구의 꺼지는 시간 중 이른 시간을 y에 담기
    x = arr[t][0] if arr[t][0] > arr[t][2] else arr[t][2]
    y = arr[t][3] if arr[t][1] > arr[t][3] else arr[t][1]
    if y - x > 0:
        print(f'#{t+1} {y-x}')
    else:
        print(f'#{t+1} 0')