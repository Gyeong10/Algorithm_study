N = int(input())
area = [[0]*100 for _ in range(100)]
total = 0
for n in range(N):
    a,b = map(int,input().split())

    for i in range(a,a+10):
        for j in range(b,b+10):
            if area[i][j] == 0:
                area[i][j] = 1
                total += 1

print(total)