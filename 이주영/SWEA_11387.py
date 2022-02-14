# 데미지 총량 구하기
# 처음에는 기본 데미지, 두번째부터 추가데미지가 생김 (지금까지 한 공격의 횟수 활용)
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    total = arr[t][0]
    for i in range(1, arr[t][2]):
        total += arr[t][0] * (1 + arr[t][1] * i / 100)
    print(f'#{t+1} {int(total)}')