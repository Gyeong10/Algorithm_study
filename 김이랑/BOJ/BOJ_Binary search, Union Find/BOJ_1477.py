N, M, L = map(int, input().split())
store = list(map(int, input().split()))
store.sort()
dis = [store[0],]
for i in range(N-1):
    dis.append(store[i+1]-store[i])
dis.append(L-store[-1])
dis.sort()

for i in range(M):
    now = dis.pop()
    dis.append(now//2)
    dis.append(now-(now//2))
    dis.sort()

print(dis[-1])