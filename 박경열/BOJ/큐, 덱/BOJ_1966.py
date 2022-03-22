# 1966 프린터 큐

import sys

sys.stdin = open('BOJ_1966.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    queue = list(range(N))

    target = queue[M]

    cnt = 0
    while True:

        if arr[0] == max(arr):
            if queue[0] == target:
                break
            else:
                cnt += 1
                arr.pop(0)
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
            arr.append(arr.pop(0))

    print(cnt + 1)