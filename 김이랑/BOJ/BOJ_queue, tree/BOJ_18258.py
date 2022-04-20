from collections import deque
N = int(input())
queue = deque()
queue += list(range(1, N+1))

flag = 1
while queue:
    if len(queue) == 1:
        print(queue.popleft())
    elif flag:
        queue.popleft()
        flag = 0
    else:
        temp = queue.popleft()
        queue.append(temp)
        flag = 1

