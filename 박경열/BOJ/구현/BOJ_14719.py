import sys; sys.stdin = open('BOJ_14719.txt')

H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(H):
    temp = 0
    flag = 0
    for j in range(W):
        if block[j]:
            block[j] -= 1
            flag = 1
            ans += temp
            temp = 0
        elif flag:
            temp += 1

print(ans)