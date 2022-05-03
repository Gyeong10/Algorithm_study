N, K = map(int, input().split())
values = [0] * (K+1)
for i in range(N):
    W, V = map(int, input().split())
    for j in range(K, W-1, -1):
        values[j] = max(values[j], values[j-W]+V)

print(values[-1])