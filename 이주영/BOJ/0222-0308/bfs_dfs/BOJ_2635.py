num = int(input())
result = []
for two in range(1, num+1):
    arr = [num, two]
    i = 1
    while True:
        next_num = arr[i - 1] - arr[i]
        if next_num < 0:
            break
        arr.append(next_num)
        i += 1

    if len(result) < len(arr):
        result = arr
print(len(result))
for k in result:
    print(k, end=' ')