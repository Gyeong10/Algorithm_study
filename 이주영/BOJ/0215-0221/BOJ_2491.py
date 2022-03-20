n = int(input())
arr = list(map(int, input().split()))
cnt = max_cnt = 1
for i in range(n-1):
    if arr[i+1] - arr[i] >= 0:
        cnt += 1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
cnt = 1
for i in range(n-1):
    if arr[i+1] - arr[i] <= 0:
        cnt += 1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)