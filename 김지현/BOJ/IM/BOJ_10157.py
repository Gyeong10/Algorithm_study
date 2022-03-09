r, c = map(int,input().split())
K = int(input())

arr = [[0]*c for _ in range(r)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ni = nj = cnt = 0
n = 1
arr[ni][nj] = n
if K > r*c:
    print(0)

else:
    while n < K:
        n += 1
        ni += di[cnt]
        nj += dj[cnt]

        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] == 0:
            arr[ni][nj] = n
        else:
            ni -= di[cnt]
            nj -= dj[cnt]
            cnt = (cnt+1)%4
            ni += di[cnt]
            nj += dj[cnt]
            arr[ni][nj] = n
    print(ni+1, nj+1)
