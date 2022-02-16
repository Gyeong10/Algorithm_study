# 합집합 면적 구하기

# 가장 큰 x와 y를 구하여 그 크기만큼의 판을 만들어줌
# 네모 안에 들어가는 칸은 모두 1을 넣어주고 1의 개수를 출력

arr = [list(map(int, input().split())) for _ in range(4)]
max_x = max_y = cnt = 0
for i in range(4):
    max_x = arr[i][2] if arr[i][2] > max_x else max_x
    max_y = arr[i][3] if arr[i][3] > max_y else max_y
result = [[0] * max_x for _ in range(max_y)]
for dot in arr:
    for i in range(dot[1], dot[3]):
        for j in range(dot[0], dot[2]):
            result[i][j] = 1
for i in range(max_y):
    for j in range(max_x):
        if result[i][j]:
            cnt += 1
print(cnt)


# 겹치는 거 빼니까 3번 겹치는 건 3번 다 빠져서 이렇게는 안되겠다 싶어서 포기..
# arr = [list(map(int, input().split())) for _ in range(4)]
# result = 0
# for i in range(4):
#     result += (arr[i][2]-arr[i][0]) * (arr[i][3]-arr[i][1])
# for i in range(3):
#     for j in range(i+1, 4):
#         if arr[j][0] >= arr[i][2]:
#             continue
#         else:
#             x1 = arr[j][0] if arr[j][0] > arr[i][0] else arr[i][0]
#             x2 = arr[j][2] if arr[j][2] < arr[i][2] else arr[i][2]
#             y1 = arr[j][1] if arr[j][1] > arr[i][1] else arr[i][1]
#             y2 = arr[j][3] if arr[j][3] < arr[i][3] else arr[i][3]
#         result -= (x2-x1) * (y2-y1)
# print(result)