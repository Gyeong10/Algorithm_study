stones = [2,4,5,3,2,1,4,2,5,1]
k = 3

def check(stones, n, k):
    cnt = 0
    for i in stones:
        if i < n:
            cnt += 1
            if cnt >= k:
                return n-1
        else:
            cnt = 0
    return n

def solution(stones, k):
    l, r = 1, max(stones)
    while l < r:
        mid = (l+r)//2
        n = check(stones, mid, k)
        if n < mid:
            r = n
        else:
            l = mid + 1
    return l

print(solution(stones, k))