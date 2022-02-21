w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
xs = [0]  # 가로 점선
ys = [0]  # 세로 점선
for i in range(n):
    if arr[i][0]:
        ys.append(arr[i][1])
    else:
        xs.append(arr[i][1])
xs.sort()
ys.sort()
xs.append(h)
ys.append(w)
max_area = 0
for i in range(len(xs)-1):
    for j in range(len(ys)-1):
        area = (xs[i+1] - xs[i]) * (ys[j+1] - ys[j])
        if max_area < area:
            max_area = area
print(max_area)