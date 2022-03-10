n = int(input())
arr = list(map(int, input().split()))
cnt = 0
p = [0] * n
visited = [0] * n
max_value = max(arr)
min_idx = 0
while cnt < n:
    for i in range(n):
        if max_value == arr[i]:
            min_idx = i
    for i in range(n-1, -1, -1):
        if arr[min_idx] >= arr[i] and not visited[i]:
            min_idx = i
    visited[min_idx] = 1
    p[min_idx] = cnt
    cnt += 1
print(*p)