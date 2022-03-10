C = int(input())
for c in range(C):
    arr = list(map(int, input().split()))
    total = sum(arr[1:])
    avg = total / arr[0]
    cnt = 0
    for i in range(1, arr[0]+1):
        if arr[i] > avg:
            cnt += 1
    print(f'{(cnt/arr[0]*100):.3f}%')