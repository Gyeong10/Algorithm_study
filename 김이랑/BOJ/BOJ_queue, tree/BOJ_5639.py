num_list = []
while 1:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def post_order(left, right):
    if left > right:
        return
    else:
        root = num_list[left]
        new_root = right+1
        for i in range(left+1, right+1):
            if root<num_list[i]:
                new_root = i
                break
        post_order(left+1, new_root-1)
        post_order(new_root, right)
        print(root)

post_order(0, len(num_list)-1)