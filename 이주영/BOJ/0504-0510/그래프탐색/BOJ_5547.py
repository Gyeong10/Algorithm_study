import sys
W, H = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
# i가 짝수일 때 왼쪽 아래에 있는 정육각형 좌표 (i+1, j) 왼쪽 위 : (i-1, j)
# i가 홀수일 때 오른쪽 아래에 있는 정육각형 좌표 (i+1, j) 오른쪽 위 : (i-1, j)
cnt = 0
for i in range(H):
    for j in range(W):
        if arr[i][j]:
            continue
        if i % 2:
            for di, dj in [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj]:
                    cnt += 1

        else:
            for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj]:
                    cnt += 1
print(cnt)