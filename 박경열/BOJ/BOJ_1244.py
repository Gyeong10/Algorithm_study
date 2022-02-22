# 스위치 켜고 끄기

import sys

N = int(sys.stdin.readline())
switch =[0] + list(map(int, sys.stdin.readline().split()))
stu = int(sys.stdin.readline())

students = []
for i in range(stu):
    a, b = map(int, sys.stdin.readline().split())
    students += [[a, b]]

for i in range(len(students)):
    num = students[i][1]

    if students[i][0] == 1:
        for j in range(1, N//num + 1):
            if switch[num * j]:
                switch[num * j] = 0
            else:
                switch[num * j] = 1
    else:
        if switch[num]:
            switch[num] = 0
        else:
            switch[num] = 1

        x = 1
        while 0 < num - x <= N and 0 < num + x <= N:
            if switch[num - x] != switch[num + x]:
                break
            else:
                if switch[num - x]:
                    switch[num - x] = 0
                    switch[num + x] = 0
                else:
                    switch[num - x] = 1
                    switch[num + x] = 1
                x += 1

cnt = 1
for i in range(1, N+1):
    if cnt != 21:
        print(switch[i], end=' ')
    else:
        cnt = 1
        print()
        print(switch[i], end=' ')
    cnt += 1