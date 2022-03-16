# 왜 틀렸을까요..ㅜㅜ

# 가로 세로 각각 가장 긴 변을 찾아
# 가장 긴 가로변 양 옆 인덱스의 값의 차이 = 작은 사각형의 세로변
# 가장 긴 세로변 양 옆 인덱스의 값의 차이 = 작은 사각형의 가로변
k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
max_x_idx = max_y_idx = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[max_y_idx][1] < arr[i][1]:
            max_y_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if arr[max_x_idx][1] < arr[i][1]:
            max_x_idx = i
# 가장 긴 가로 세로변 각각 할당
max_x = arr[max_x_idx][1]
max_y = arr[max_y_idx][1]
# 인덱스가 0~5만 나오게 하기 위해 6으로 나눈 나머지 사용
small_x = abs(arr[(max_y_idx-1) % 6][1] - arr[(max_y_idx+1) % 6][1])
small_y = abs(arr[(max_x_idx-1) % 6][1] - arr[(max_x_idx+1) % 6][1])

print(((max_x * max_y) - (small_x * small_y)) * k)