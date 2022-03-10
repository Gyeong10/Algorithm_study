import sys

input_num = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
# 뒤부터 거꾸로 쌓임
output_list = [-1]

for i in range(input_num-2, -1, -1):

    if stack[i] < stack[i+1]:
        output_list.append(stack[i+1])
    elif stack[i] < output_list[-1]:
        output_list.append(output_list[-1])
    else:
        idx = i + 2
        flag = 1
        while idx < input_num:
            if stack[idx] > stack[i]:
                output_list.append(stack[idx])
                flag = 0
                break
            else:
                idx += 1
        if flag:
            output_list.append(-1)

for i in range(len(output_list)-1, -1, -1):
    print(output_list[i], end=' ')