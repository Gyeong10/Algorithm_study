# 딱지놀이

# 카운팅 정렬 변형해서 사용
# A와 B의 딱지에서 1, 2, 3, 4 의 개수를 세어 cnt배열에 저장
# 4부터 비교하며 개수가 큰 쪽을 출력

n = int(input())
for t in range(n):
    cards = [x for x in range(4)]
    cnt = [[0] * 4 for _ in range(2)]
    arr = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, arr[0][0]+1):
        for j in range(4):
            cnt[0][arr[0][i]-1] += 1
    for i in range(1, arr[1][0]+1):
        for j in range(4):
            cnt[1][arr[1][i]-1] += 1
    for i in range(3, -1, -1):
        if cnt[0][i] > cnt[1][i]:
            print('A')
            break
        elif cnt[0][i] < cnt[1][i]:
            print('B')
            break
    else:
        print('D')