import sys
sys.stdin = open("test_2001_input.txt", "r")

test_num = int(input())
for test_case in range(1, test_num + 1):
    grid_size, flapper_size = map(int, input().split())
    grid = []
    # 파리채 그리드 만들기
    for i in range(grid_size):
        grid.append(list(map(int, input().split())))

    max = 0

    # i, j 좌표를 기준으로 파리채 사이즈만큼 포문 돌기
    for i in range(grid_size):
        for j in range(grid_size):
            # i, j 좌표 바뀔 때 death 초기화 들어가야함
            death = 0
            # range로 조건 만들면 실행 속도 더 빨라질수도 있겠다
            # 이 방법은 이프문을 다 도니까 몇개 더 돌긴함
            for k in range(flapper_size):
                for l in range(flapper_size):
                    # 그리드 벗어나면 death에 저장안함
                    if i+k < grid_size and j+l < grid_size:
                        death = grid[i+k][j+l] + death
            if death > max:
                max = death

    print(f'#{test_case} {max}')