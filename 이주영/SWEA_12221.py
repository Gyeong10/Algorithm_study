# 9*9만 가능한 구구단
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    if arr[t][0] > 9 or arr[t][1] > 9:
        print(f'#{t+1} -1')
    else:
        print(f'#{t+1} {arr[t][0] * arr[t][1]}')