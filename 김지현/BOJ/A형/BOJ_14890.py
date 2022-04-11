import sys

def check(road):
    global cnt
    isslope = [0]*N
    for i in range(N-1):
        if road[i] == road[i+1]:
            continue
        # 절댓값 차이가 2이상 나면 아무것도 X
        elif abs(road[i] - road[i+1]) >= 2:
            return
        # 경사로 필요
        elif abs(road[i] - road[i+1]) == 1:
            # 경사로 설치여부 확인
            if slope(road, i, isslope):
                continue
            else:
                return
    cnt += 1
    return

def slope(a, idx, isslope):
    # 같은 레벨 갯수
    n = 0
    # 순방향일 때
    if a[idx] > a[idx+1]:
        t = a[idx+1]
        idx = idx + 1
        while 0 <= idx < N and n < L and not isslope[idx]:
            if a[idx] == t:
                isslope[idx] = 1
                n += 1
            else:
                break
            idx += 1
    # 역방향
    elif a[idx+1] > a[idx]:
        t = a[idx]
        while 0 <= idx < N and n < L and not isslope[idx]:
            if a[idx] == t:
                isslope[idx] = 1
                n += 1
            else:
                break
            idx -= 1
    if n == L:
        return True
    return False

N, L = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0

# 가로
for i in range(N):
    check(arr[i])
# 세로
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(arr[j][i])
    check(temp)

print(cnt)