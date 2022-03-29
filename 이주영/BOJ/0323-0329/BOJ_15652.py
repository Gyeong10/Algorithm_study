def perm(n, lst):
    if len(lst) == M:
        print(*lst, sep=' ')
        return
    for i in range(1, n+1):
        if lst and lst[-1] > i:
            continue
        perm(n, lst + [i])

N, M = map(int, input().split())
perm(N, [])