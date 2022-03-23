T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append([i, doc[i]])
    cnt = 0
    while q:
        max_V = max(t[1] for t in q)
        if max_V == q[0][1]:
            n = q.pop(0)
            cnt += 1
            if n[0] == M:
                print(cnt)
                break
        else:
            q.append(q.pop(0))