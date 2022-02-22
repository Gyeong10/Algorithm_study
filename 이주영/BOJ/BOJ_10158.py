# 시간 초과.. 라는데 방법을 못찾았어요,, 테케는 다 출력됩니다
w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())
dq = [1, 1, -1, 1, 1, -1, -1, 1, -1, -1]
dp = [1, -1, -1, -1, 1, 1, -1, -1, -1, 1]
k = 0
for t in range(T):
    p += dp[k]
    q += dq[k]
    if p == 0 and q == h:
        k = 1
    elif p == w and q == 0:
        k = 5
    elif p == 0 and q == 0:
        k = 4
    elif p == w and q == h:
        k = 2
    elif p < 0 or q < 0 or p > w or q > h:
        p -= dp[k]
        q -= dq[k]
        k = (k+1) % 10
        p += dp[k]
        q += dq[k]

print(p, q)