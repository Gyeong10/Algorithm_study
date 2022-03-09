arr = [int(input()) for _ in range(9)]
# 부분집합
for i in range(1 << 9):
    total = 0
    result = []
    n = 0
    for j in range(9):
        if i & (1 << j):
            total += arr[j]
            result.append(arr[j])
            n += 1
    # 키합 = 100, 원소갯수 7개
    if total == 100 and n == 7:
        break
# 선택 정렬
for i in range(6):
    minIdx = i
    for j in range(i+1,7):
        if result[minIdx] > result[j]:
            minIdx = j
    result[i], result[minIdx] = result[minIdx], result[i]

for i in result:
    print(i)



