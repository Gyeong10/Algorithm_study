import sys; sys.stdin = open('BOJ_2110.txt')

N, C = map(int, sys.stdin.readline().split())
house = [0] * N
for i in range(N):
    house[i] = int(sys.stdin.readline())
house.sort()

start = 0
end = house[-1] - house[0]

ans = 0
while start <= end:
    # middle = 간격
    middle = (start + end) // 2
    cnt = 1
    temp = house[0]
    # 1 2 4 8 9
    for i in range(1, N):
        if house[i] >= temp + middle:
            temp = house[i]
            cnt += 1

    if cnt >= C:
        ans = middle
        start = middle + 1
    else:
        end = middle - 1

print(ans)