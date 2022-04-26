N, M, L = map(int, input().split())
store = list(map(int, input().split()))
store.append(0)
store.append(L)
store.sort()

start = 0
end = store[-1]
answer = 0

while start <= end:
    cnt = 0
    mid = (start+end)//2

    if end == 0:
        break
    elif mid == 0:
        mid = 1

    for i in range(0, len(store)-1):
        if (store[i+1]-store[i]) > mid:
            cnt += (store[i+1]-store[i]-1)//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)
