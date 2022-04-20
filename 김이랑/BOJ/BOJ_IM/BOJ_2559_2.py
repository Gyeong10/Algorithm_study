M, N = map(int, input().split())
temperatures = list(map(int, input().split()))

result = []

max_total = 0
for i in range(N):
    max_total += temperatures[i]
check_total = max_total

for i in range(N, M):
    check_total = check_total - temperatures[i-N] + temperatures[i]
    if check_total > max_total:
        max_total = check_total

print(max_total)