import sys
import copy

def move(dir):
    # 위로 합치기
    if dir == 0:
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    # 0이면 빈칸이니까 옮기기만 함
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    # 같으면 2배 곱하기
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp*2
                        idx += 1
                    # 다른 값이면 그 위에 쌓여하하므로 idx += 1 하고 값저장
                    else:
                        idx += 1
                        arr[idx][j] = temp
    # 아래로 합치기
    elif dir == 1:
        for j in range(N):
            idx = N-1
            for i in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][j] = temp
    # 오른쪽으로 합치기
    elif dir == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = temp
    # 왼쪽으로 합치기
    else:
        for i in range(N):
            idx = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = temp



def dfs(n):
    global arr, max_V
    # 5번 되면
    if n == 5:
        # 최댓값을 찾는다.
        for i in range(N):
            for j in range(N):
                max_V = max(max_V, arr[i][j])
        return
    # 임시 arr에 회전하기 전 상태 저장해 뒀다가
    temp_arr = copy.deepcopy(arr)
    for i in range(4):
        move(i)
        dfs(n+1)
        # 다음번에 다시 초기화해줌
        arr = copy.deepcopy(temp_arr)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_V = 0
dfs(0)
print(max_V)

