len_num_list = int(input())
num_list = list(map(int, input().split()))

max_count = 0
if len(num_list) == 1:
    max_count = 1
elif len(num_list) > 1:
    same_count = 0
    if num_list[1] > num_list[0]:
        direction = 'up'
    elif num_list[1] < num_list[0]:
        direction = 'down'
    else:
        direction = 'same'
        same_count = 1

    check = num_list[1]
    count = 2
    max_count = 2

    for i in range(2, len_num_list):
        if num_list[i] > check:
            now_direction = 'up'
        elif num_list[i] < check:
            now_direction = 'down'
        else:
            now_direction = direction
            if same_count:
                same_count += 1
            else:
                same_count = 1

        if direction != now_direction and same_count > 0:
            count = same_count + 2
            same_count = 0
            if count > max_count:
                max_count = count
        elif direction == now_direction or direction == 'same':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 2

        check = num_list[i]
        direction = now_direction

print(max_count)
