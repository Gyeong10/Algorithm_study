import copy

pos_r = [1, 1]
pos_c = [1, -1]


N = int(input())


def dfs(C, D, arr):
    global count
    if D == N:
        count += 1
        return
    else:
        visited = copy.deepcopy(arr[1:])

        for i in range(0, len(visited)):
            visited[i][C] = True
            if C + (i+1) < N:
                if not visited[i][C + (i+1)]:
                    visited[i][C + (i+1)] = True
            if 0 <= C -(i+1) :
                if not visited[i][C -(i+1)]:
                    visited[i][C -(i+1)] = True
        if D+1 == N:
            dfs(0, D+1, visited)
        else:
            if bool(visited[0]):
                for i in range(N):
                    if not visited[0][i]:
                        dfs(i, D+1, visited)
                return


count = 0

for i in range(N):
    arr = [[False]*N for _ in range(N)]
    dfs(i, 0, arr)

print(count)