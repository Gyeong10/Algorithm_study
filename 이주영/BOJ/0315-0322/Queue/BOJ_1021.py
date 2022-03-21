import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
# 큐에 인덱스 담아놓기
q = deque([i for i in range(1, N+1)])
# 연산 횟수
cnt = 0
# 각 숫자별로
for num in nums:
    while True:
        # 숫자랑 q의 첫번째 원소와 같으면 pop하고 다음 숫자로 변경
        if q[0] == num:
            q.popleft()
            break
        # num이 있는 index가 길이의 반보다 작으면 왼쪽으로 회전
        if q.index(num) < len(q) / 2:
            q.append(q.popleft())
            cnt += 1
        # 아니면 오른쪽으로 회전
        else:
            q.appendleft(q.pop())
            cnt += 1
print(cnt)

