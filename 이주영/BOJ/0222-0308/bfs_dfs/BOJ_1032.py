n = int(input())
arr = [input() for _ in range(n)]
result = ''
for j in range(len(arr[0])):
    for i in range(n-1):
        if arr[i][j] != arr[i+1][j]:
            result += '?'
            break
    else:
        result += arr[0][j]
print(result)