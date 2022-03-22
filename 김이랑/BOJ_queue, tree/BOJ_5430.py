from collections import deque
import sys

for i in range(int(sys.stdin.readline())):
    operates = list(map(str, sys.stdin.readline()))
    dq_len = int(sys.stdin.readline())
    dq = deque()
    if dq_len != 0:
        num = list(map(int, sys.stdin.readline()[1:-2:1].split(',')))
        dq += num
    else:
        trash = sys.stdin.readline()
    flag = 0
    for operator in operates:
        if operator == 'R':
            dq.reverse()
        if operator == 'D':
            if len(dq) == 0:
                flag = 1
                break
            else:
                dq.popleft()

    if flag:
        print('error')
    else:
        answer = []
        for d in dq:
            answer.append(d)
        print(answer)