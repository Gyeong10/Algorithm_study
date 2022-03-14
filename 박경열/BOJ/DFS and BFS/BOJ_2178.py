# 2178 미로 탐색

import sys

def bfs():
    queue = [[1, 1]]
    visited[1][1] = 1
    while queue:
        t = queue.pop(0)
        if t == [N, M]:
            return
        for i in range(4):
            if arr[t[0]+dx[i]][t[1]+dy[i]] and not visited[t[0]+dx[i]][t[1]+dy[i]]:
                queue.append([t[0]+dx[i], t[1]+dy[i]])
                visited[t[0]+dx[i]][t[1]+dy[i]] = visited[t[0]][t[1]] + 1


N, M = map(int, sys.stdin.readline().split())
arr = [[0] * (M+2)] + [[0] + list(map(int, sys.stdin.readline().rstrip())) + [0] for _ in range(N)] + [[0] * (M+2)]
visited = [[0]*(M + 2) for _ in range(N + 2)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
bfs()
print(visited[N][M])