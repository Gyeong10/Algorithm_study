# 24시간 표현법
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
# 처음 시간에서 지난 시간을 더해 24로 나눈 나머지 == 현재 시간
for t in range(T):
    print(f'#{t+1} {(arr[t][0] + arr[t][1]) % 24}')