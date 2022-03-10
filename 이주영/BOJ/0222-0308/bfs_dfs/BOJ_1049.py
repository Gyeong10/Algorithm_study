import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
min_six, min_one = arr[0][0], arr[0][1]
for i in range(m):
    if min_six > arr[i][0]:
        min_six = arr[i][0]
for i in range(m):
    if min_one > arr[i][1]:
        min_one = arr[i][1]
if min_six > min_one * 6:   # 다 낱개로
    total = min_one * n
elif (n % 6) * min_one < min_six:   # 세트 되는 건 세트로 나머지는 낱개
    total = ((n // 6) * min_six) + ((n % 6) * min_one)
else:   # 세트로 좀더 많이 사는게 이득
    total = ((n // 6) + 1) * min_six
print(total)