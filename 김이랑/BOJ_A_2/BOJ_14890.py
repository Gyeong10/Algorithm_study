N, L = map(int, input().split())
row_grid = [list(map(int, input().split())) for _ in range(N)]
col_grid = []

for j in range(N):
    temp = []
    for i in range(N):
        temp.append(row_grid[i][j])
    col_grid.append(temp)


def check(arr):
    global total_road
    used = [False]*N
    i = 0
    while i < N-1:
        if arr[i] == arr[i+1]:
            i += 1
        #낮아질떄, 앞을 조사
        elif arr[i] - arr[i+1] == 1:
            if i + L < N:
                for j in range(i+1, i+L+1, 1):
                    if arr[i+L] != arr[j] or used[j]:
                        return
                    else:
                        used[j] = True
                i += L
            else:
                return
        # 높아질때, 뒤를 조사
        elif arr[i+1] - arr[i] == 1:
            if 0 <= i - L + 1:
                for j in range(i-L+1, i+1, 1):
                    if arr[i] != arr[j] or used[j]:
                        return
                    else:
                        used[j] = True
                i += 1
            else:
                return
        # 2 이상 차이남
        else:
            return
    total_road += 1


total_road = 0


for i in range(N):
    check(row_grid[i])
    check(col_grid[i])


print(total_road)