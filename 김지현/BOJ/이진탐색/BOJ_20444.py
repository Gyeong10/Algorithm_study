n, k = map(int, input().split())

left = 0
right = n // 2
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = (mid + 1)*(n-mid+1)

    if cnt == k:
        ans = 1
        break
    elif cnt > k:
        right = mid - 1
    else:
        left = mid + 1

if ans:
    print('YES')
else:
    print('NO')