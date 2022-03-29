def perm(lst, cnt):
    if cnt == M:
        print(*lst, sep=' ')
        return
    for i in range(1, N+1):
        if i in lst:
            continue
        perm(lst+[i], cnt+1)


N, M = map(int, input().split())
perm([], 0)