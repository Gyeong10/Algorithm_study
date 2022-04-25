N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
# 하우스 정렬
house.sort()
s = 1
e = house[-1] - house[0]
ans = 0
while s <= e:
    mid = (s+e)//2
    current = house[0]
    cnt = 1

    for i in range(1, N):
        if house[i] >= current + mid:
            cnt += 1
            current = house[i]
    if cnt >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)