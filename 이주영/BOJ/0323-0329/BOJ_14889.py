def solve(lst1, lst2, idx):
    global min_val
    if idx == N:
        # 계산
        lst1_sum = 0
        lst2_sum = 0
        for i in range(N//2):
            for j in range(N//2):
                lst1_sum += arr[lst1[i]][lst1[j]]
                lst2_sum += arr[lst2[i]][lst2[j]]
        val = abs(lst1_sum - lst2_sum)
        if min_val > val:
            min_val = val

    if len(lst1) < N//2:
        solve(lst1 + [idx], lst2, idx+1)
    if len(lst2) < N//2:
        solve(lst1, lst2 + [idx], idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_val = 100*400
solve([], [], 0)
print(min_val)