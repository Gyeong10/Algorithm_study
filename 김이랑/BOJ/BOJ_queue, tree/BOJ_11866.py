from collections import deque

N, K = map(int, input().split())
queue = deque()
queue += list(range(1, N+1))
output = []
while queue:
    for i in range(K-1):
        temp = queue.popleft()
        queue.append(temp)
    temp = queue.popleft()
    output.append(str(temp))
answer = ", ".join(output)
print(f'<{answer}>')