num_list = []
while 1:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break


def post_order(root_idx, end_idx):
    if end_idx <= root_idx + 1:
        return
    else:
        root = num_list[root_idx]
        new_idx = 0
        for i in range(root_idx+1, end_idx):
            if root < num_list[i]:
                new_idx = i
                break
        post_order(root_idx+1, new_idx)
        post_order(new_idx, end_idx)
        print(root)


post_order(0, len(num_list))