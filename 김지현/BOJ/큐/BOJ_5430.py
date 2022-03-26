import sys
from _collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = list(sys.stdin.readline().strip('\n'))
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip('['']''\n')
    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr.split(',')))
        arr = deque(arr)
    flag = 1
    is_r = False
    for i in p:
        if i == 'R':
            is_r = not is_r
        if i == 'D':
            if arr:
                if is_r:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                flag = 0
                break
    if is_r:
        arr.reverse()
    if flag:
        print(str(list(arr)).replace(' ', ''))
    else:
        print('error')
