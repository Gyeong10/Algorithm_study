# 색종이
# 마지막 조건이 시간초과 나서 각 네모의 값을 넣는 과정을 한번에 넣는 걸로 바꿨더니 통과됐어염...

# 1001 * 1001 판 만들고 네모 숫자를 순서대로 집어넣으면 앞에 넣은 숫자가 뒤에 넣은 숫자에 가리니까
# 다 넣고 나서 숫자를 세어주었음
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * 1001 for _ in range(1001)]
cnt = [0] * N
for k in range(N):
    for i in range(arr[k][1], arr[k][1]+arr[k][3]):
        result[i][arr[k][0]:arr[k][0]+arr[k][2]] = [k+1] * arr[k][2]  # 이부분..!
for k in range(1, N+1):
    for i in range(1001):
        cnt[k-1] += result[i].count(k)   # 뭐가 틀린지 몰라서 이것도 고쳤었음 함수사용!
        print(*cnt, sep='\n')



# 53점.. (마지막 조건 시간초과)
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# max_x = max_y = 0
# for i in range(N):
#     max_x = arr[i][0]+arr[i][2] if arr[i][0]+arr[i][2] > max_x else max_x
#     max_y = arr[i][1]+arr[i][3] if arr[i][1]+arr[i][3] > max_y else max_y
# result = [[0] * max_x for _ in range(max_y)]
# cnt = [0] * N
# for k in range(N):
#     for i in range(arr[k][1], arr[k][1]+arr[k][3]):
#         for j in range(arr[k][0], arr[k][0]+arr[k][2]):
#             result[i][j] = k+1
# for i in range(max_y):
#     for j in range(max_x):
#         for k in range(1, N+1):
#             if result[i][j] == k:
#                 cnt[k-1] += 1
# print(*cnt, sep='\n')