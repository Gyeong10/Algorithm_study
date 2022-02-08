# 파리퇴치
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이려고 할 때, 최대값 구하기
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    # 아래쪽으로 이동(x값)
    for startx in range(n-m+1):
        # 오른쪽로 이동(y값)
        for starty in range(n-m+1):
            total = 0
            # index값이 startx인 곳부터 startx+m인 곳까지 사용
            for i in range(startx, startx + m):
                # x는 고정하고 y에 index값이 starty인 곳부터 starty+m인 곳까지 더해서 total에 더해줌
                total += sum(arr[i][starty:starty+m])
            # result보다 total이 크면 total을 result에 할당해주고 아니면 그대로 넘어간다.
            result = total if total > result else result
    print(f'#{t} {result}')