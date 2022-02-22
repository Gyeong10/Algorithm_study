N = int(input())
area = [[0]*1001 for _ in range(1001)]

for n in range(1,N+1):
    x, y, w, h = map(int, input().split())
    for i in range(y, y+h):
        area[i][x:(x+w)] = [n]*w

for n in range(1,N+1):
    cnt = 0
    for i in range(1001):
        cnt += area[i].count(n)
    print(cnt)