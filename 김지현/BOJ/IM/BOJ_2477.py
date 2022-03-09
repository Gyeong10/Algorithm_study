n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
w = h = 0
w_idx = h_idx = 0
#큰사각형 가로,세로 구하기
for i in range(6):
    #가로
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > w:
            w = arr[i][1]
            w_idx = i
    #세로
    else:
        if arr[i][1] > h:
            h = arr[i][1]
            h_idx = i

#작은사각형 가로,세로 구하기
s_w = abs(arr[(w_idx-1)%6][1] - arr[(w_idx+1)%6][1])
s_h = abs(arr[(h_idx-1)%6][1] - arr[(h_idx+1)%6][1])

print((w*h-s_w*s_h)*n)