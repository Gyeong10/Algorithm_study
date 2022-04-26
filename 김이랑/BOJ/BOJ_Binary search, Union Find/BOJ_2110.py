N, C = map(int, input().split())

grid = [int(input()) for _ in range(N)]
grid.sort()

start = 1
end = grid[-1] - grid[0]
result = 0

while start <= end:
    mid = (start+end)//2
    count = 1
    current = grid[0]

    for i in range(1, N):
        if mid <= grid[i] - current:
            count += 1
            current = grid[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
