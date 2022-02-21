# 시간 초과.. ㅜㅜ
n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_total = sum(arr[:k])
for i in range(n-k+1):
    total = 0
    for j in range(k):
        total += arr[i+j]
    if max_total < total:
        max_total = total
print(max_total)


# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# max_total = sum(arr[:k])
#
# for i in range(k, n):
#     if arr[i] > arr[i-k]:
#         max_total += arr[i] - arr[i-k]
#     else:
#
# print(max_total)