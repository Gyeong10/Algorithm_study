# 예제 4 입력 불통
import sys
from collections import deque

# def search(q, cnt):
#     global min_cnt
#     for want in arr:
#         if visited[want]:
#             continue
#         while q:
#             if q[0] == want:
#                 visited[q.popleft()] = 1
#                 break
#             if q.index(want) < len(q) // 2:
#                 tmp = q.popleft()
#                 q.append(tmp)
#                 cnt += 1
#             elif q.index(want) > len(q) // 2:
#                 tmp = q.pop()
#                 q.appendleft(tmp)
#                 cnt += 1
#             else:
#                 tmp = q
#                 tmp.append(tmp.popleft())
#                 search(tmp, cnt+1)
#                 q.appendleft(q.pop())
#                 search(q, cnt+1)
#     if min_cnt > cnt:
#         min_cnt = cnt


# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# q = deque()
# min_cnt = N*M
# visited = [0] * (N+1)
# for i in range(1, N+1):
#     q.append(i)
# search(q, 0)
# print(min_cnt)

def dfs(q, cnt):
    global min_cnt, now
    if now == M:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    want = arr[now]
    while q:
        if q[0] == want:
            visited[q.popleft()] = 1
            now += 1
            return
        if q.index(want) < len(q) // 2:
            tmp = q.popleft()
            q.append(tmp)
            search(q, cnt+1)
        elif q.index(want) > len(q) // 2:
            tmp = q.pop()
            q.appendleft(tmp)
            search(q, cnt+1)
        else:
            tmp = q
            tmp.append(tmp.popleft())
            search(tmp, cnt+1)
            q.appendleft(q.pop())
            search(q, cnt+1)


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
q = deque()
min_cnt = N * M
visited = [0] * (N + 1)
for i in range(1, N + 1):
    q.append(i)
now = 0
search(q, 0)
print(min_cnt)