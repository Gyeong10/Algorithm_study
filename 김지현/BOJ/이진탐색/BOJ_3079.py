import sys

N, M = map(int, sys.stdin.readline().split())
t = [int(sys.stdin.readline()) for _ in range(N)]

left = min(t)
right = max(t) * M
ans = right
while left <= right:
    # 사람의 수
    total = 0
    # 총 시간
    mid = (left + right) // 2
    # 검색대에서 검사할 수 있는 사람의 수 구하기
    for i in range(N):
        total += mid // t[i]

    if total >= ans:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)