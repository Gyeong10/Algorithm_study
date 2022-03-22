# 5430 AC

import sys
from collections import deque

sys.stdin = open('BOJ_5430.txt')

def solve():
    global flag, ans

    for i in p:
        if i == 'R':
            if flag:
                flag = 0
            else:
                flag = 1

        else:
            if queue:
                if flag:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                ans = 0
                return


T = int(sys.stdin.readline())
for _ in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()
    queue = deque()

    s = ''
    for i in range(len(x)-1):
        if x[i] != '[' and x[i] != ']' and x[i] != ',':
            s += x[i]
            if x[i+1] == ',' or x[i+1] == ']':
                queue.append(int(s))
                s = ''

    flag = 1
    ans = 1
    solve()

    if queue:
        if not flag:
            queue.reverse()

        print('[', end='')
        for q in range(len(queue)-1):
            print(queue[q], end=',')
        print(f'{queue.pop()}]')

    else:
        if ans:
            print('[]')
        elif ans == 0:
            print('error')