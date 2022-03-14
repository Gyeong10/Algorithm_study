# 본인 왼쪽, 본인, 본인 오른쪽 숫자 중 본인이 중간인 숫자 개수 찾기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # 차이의 곱이 음수면 조건 만족하므로 cnt에 1 더해줌
    for i in range(1, N-1):
        if (arr[i] - arr[i-1]) * (arr[i] - arr[i+1]) < 0:
            cnt += 1
    print(f'#{t} {cnt}')