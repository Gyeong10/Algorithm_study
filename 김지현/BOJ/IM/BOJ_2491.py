N = int(input())
arr = list(map(int, input().split()))
cnt = 1
max_len = 1

for i in range(1,N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_len:
        max_len = cnt
cnt = 1
for i in range(1,N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_len:
        max_len = cnt

print(max_len)
