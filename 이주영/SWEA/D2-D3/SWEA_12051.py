T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    # Broken인 두가지 경우
    # 1. Pd가 0이 아닌데(오늘 게임 적어도 1번은 이겼는데) Pg가 0(전체 이긴 퍼센트가 0)인 경우
    # 2. Pd가 100이 아닌데(오늘 게임 적어도 1번은 졌는데) Pg가 100(전체 이긴 퍼센트가 100)인 경우
    if (arr[t][1] != 0 and arr[t][2] == 0) or (arr[t][1] != 100 and arr[t][2] == 100):
        print(f'#{t+1} Broken')
    # 1~N까지 숫자 꺼내 계산 결과가 정수가 나오는 지 확인
    else:
        for today_game in range(1, arr[t][0]+1):
            # (int로 형변환해서 같은지 유무로 정수인지 확인하려 했는데 43case에서 fail 떴음.. 이유가 몰까)
            if (today_game * arr[t][1] / 100 ) == (today_game * arr[t][1] // 100):
                print(f'#{t+1} Possible')
                break
        # break 안걸리면 else문 수행
        else:
            print(f'#{t+1} Broken')