n = int(input())
arr = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    if result[arr[i]] != 0:
        for j in range(i-1,arr[i]-1,-1):
            # 칸 밀기
            result[j+1] = result[j]
    result[arr[i]] = i+1

for i in range(n-1,-1,-1):
    print(result[i], end = ' ')