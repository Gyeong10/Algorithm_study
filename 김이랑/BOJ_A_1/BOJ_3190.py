from collections import deque

N = int(input())
grid = [[1]*(N+2)]
grid += [[1]+[0]*N+[1] for _ in range(N)]
grid += [[1]*(N+2)]

# 사과는 3로 표시
K = int(input())
for i in range(K):
    r, c = map(int, input().split())
    grid[r][c] = 3

pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

L = int(input())
# 시작시간, 방향(0 오른쪽 아래, 왼쪽, 위)
order = deque()
temp = 0
for i in range(L):
    X, C = map(str, input().split())
    if C == 'L':
        temp -= 1
        if temp == -1:
            temp = 3
    else:
        temp += 1
        if temp == 4:
            temp = 0
    order.append([int(X), temp])

time = 0
now_time, now_dir = 0, 0
flag = 0


# 뱀위치
head = [1, 1]
grid[head[0]][head[1]] = 2
tail = [1, 1]

while 1:
    if order:
        next_time, next_dir = order.popleft()
    else:
        next_time, next_dir = 10000000, now_dir
    for i in range(next_time-now_time):
        time += 1
        next_head = [head[0]+pos[now_dir][0], head[1]+pos[now_dir][1]]

        if grid[next_head[0]][next_head[1]] == 0:
            grid[next_head[0]][next_head[1]] = 2
            head = next_head
            grid[tail[0]][tail[1]] = 0
            for i in range(4):
                tail_next = [tail[0]+pos[i][0], tail[1]+pos[i][1]]
                if grid[tail_next[0]][tail_next[1]] == 2:
                    tail = tail_next
                    break
        elif grid[next_head[0]][next_head[1]] == 3:
            grid[next_head[0]][next_head[1]] = 2
            head = next_head
        elif grid[next_head[0]][next_head[1]] == 1 or grid[next_head[0]][next_head[1]] == 2:
            flag = 1
            break
    now_time, now_dir = next_time, next_dir
    if flag:
        break

print(time)