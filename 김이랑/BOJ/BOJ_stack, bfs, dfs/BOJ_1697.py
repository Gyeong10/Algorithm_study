from collections import deque

s, e = map(int, input().split())

# def dfs(now, count):
#     global min
#     if now == e:
#         if count <= min:
#             min = count
#             return count
#         return count
#     elif count > min:
#         return min
#     else:
#         dfs(now+1, count+1)
#         dfs(now-1, count+1)
#         dfs(now*2, count+1)

def bfs():
    global min
    queue = deque()
    count = 0
    queue.append([s, count])
    while queue:
        temp = queue.popleft()
        now = temp[0]
        count = temp[1]
        if now == e:
            min = count
            break
        elif count > min:
            pass
        else:
            if 0 <= now < 100001 and visited[now] != 1:
                visited[now] = 1
                queue.append([now+1, count+1])
                queue.append([now*2, count+1])
                queue.append([now-1, count+1])


min = 100001
visited = [0 for i in range(100002)]
if s >= e:
    min = s-e
else:
    answer = bfs()
print(min)