from collections import deque

def check_binary(now):
    global answer
    queue = deque()
    queue.append(now)
    group_a.append(now)
    visited[now] = 1
    flag = 0
    while queue:
        now = queue.popleft()
        for next in edge[now]:
            if visited[next] == 0:
                if now in group_a:
                    if next in group_a:
                        answer = 'NO'
                        flag = 1
                        break
                    else:
                        if next not in group_b:
                            group_b.append(next)
                        queue.append(next)
                        visited[next] = 1

                else:
                    if next in group_b:
                        answer = 'NO'
                        flag = 1
                        break
                    else:
                        if next not in group_a:
                            group_a.append(next)
                        queue.append(next)
                        visited[next] = 1
        if flag:
            break


for case in range(int(input())):
    v, e = map(int, input().split())
    edge = [[] for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        edge[start].append(end)


    visited = [0] * (v+1)
    answer = 'YES'
    group_a = []
    group_b = []
    for i in range(1, v+1):
        if edge[i]:
            check_binary(i)

    print(group_a)
    print(group_b)
    print(answer)
