from collections import deque

for case in range(int(input())):
    size, num = map(int, input().split())
    queue = deque([])
    input_list = list(map(int, input().split()))
    for i in range(len(input_list)):
        if i == num:
            queue.append([1, input_list[i]])
        else:
            queue.append([0, input_list[i]])

    count = 1

    while queue:
        max_value = [0, 0]
        for i in range(len(queue)):
            if queue[i][1] > max_value[1]:
                max_value = queue[i]

        temp = queue.popleft()
        if temp[1] == max_value[1] and temp[0]:
            print(count)
            break
        elif temp[1] == max_value[1]:
            count += 1
        else:
            queue.append(temp)