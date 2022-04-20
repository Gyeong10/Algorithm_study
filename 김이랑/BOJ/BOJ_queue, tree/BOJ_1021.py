import copy
from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
queue = deque(list(range(1, N+1)))
num_list = deque(list(map(int, input().split())))

total = 0


def check_right(num):
    count = 0
    while right_queue:
        now = right_queue.popleft()
        if now == num:
            return count
        else:
            right_queue.append(now)
            count += 1


def check_left(num):
    count = 0
    while left_queue:
        now = left_queue.popleft()
        if now == num:
            return count
        else:
            left_queue.insert(0, now)
            now = left_queue.pop()
            left_queue.insert(0, now)
            count += 1


for num in num_list:
    right_queue = copy.deepcopy(queue)
    left_queue = copy.deepcopy(queue)

    right = check_right(num)
    left = check_left(num)

    if right < left:
        total += right
        queue = copy.deepcopy(right_queue)
    else:
        total += left
        queue = copy.deepcopy(left_queue)

print(total)