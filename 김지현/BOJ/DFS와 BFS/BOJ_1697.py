import sys
def bfs(a,b):
    Q = []
    Q.append(a)

    while Q:
        i = Q.pop(0)
        if i == b:
            return print(distance[i])
        
        for j in (i-1,i+1,2*i):
            if 0<=j<=m and not distance[j]:
                distance[j] = distance[i] + 1
                Q.append(j)

m = 100000
distance = [0]*(m+1)
n, k = map(int, sys.stdin.readline().split())
bfs(n,k)