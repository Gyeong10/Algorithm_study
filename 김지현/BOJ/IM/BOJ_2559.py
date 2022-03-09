
N, K = map(int, input().split())
arr = list(map(int, input().split()))
total = []
total.append(sum(arr[:K]))
for i in range(N-K):
    total.append(total[i] - arr[i] + arr[i+K])

print(max(total))