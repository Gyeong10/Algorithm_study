# 꼭짓점에 들가는거라 하나씩 더 만듦, 인덱스로 계산
grid_j, grid_i = map(int, input().split())

case_num = int(input())

# i, j 좌표 순으로 입력
shops = []

for case in range(case_num):
    direction, location = map(int, input().split())
    if direction == 1:
        shops += [0, location]
    elif direction == 2:
        shops += [grid_i, location]
    elif direction == 3:
        shops += [location, 0]
    elif direction == 4:
        shops += [location, grid_j]

check = []
direction, location = map(int, input().split())
if direction == 1:
    check += [0, location]
elif direction == 2:
    check += [grid_i, location]
elif direction == 3:
    check += [location, 0]
elif direction == 4:
    check += [location, grid_j]


answer = 0
for i in range(0, len(shops), 2):
    if abs(check[0]-shops[i]) == grid_i:
        way_1 = check[1] + shops[i+1]
        way_2 = 2*grid_j - (check[1] + shops[i+1])
        if way_1 < way_2:
            answer += (way_1 + grid_i)
        else:
            answer += (way_2 + grid_i)
    # 양옆 반대일때, 그냥 else 해도됨
    elif abs(check[1]-shops[i+1]) == grid_j:
        way_1 = check[0] + shops[i]
        way_2 = 2*grid_i - (check[0] + shops[i])
        if way_1 < way_2:
            answer += (way_1 + grid_j)
        else:
            answer += (way_2 + grid_j)
    # 나머지 방향들
    else:
        answer += (abs(check[0]-shops[i]) + abs(check[1]-shops[i+1]))
print(answer)