input_num = int(input())
input_list = []
stack = []
output_list = []
for i in range(input_num):
    input_list.append(int(input()))

list_idx = 0
for i in range(1, input_num + 1):
    while (list_idx < input_num) and (len(stack)) and (stack[-1] == input_list[list_idx]):
        stack.pop()
        list_idx += 1
        output_list.append('-')

    stack.append(i)
    output_list.append('+')

while (list_idx < input_num) and (len(stack)) and (stack[-1] == input_list[list_idx]):
    stack.pop()
    list_idx += 1
    output_list.append('-')

if (list_idx == input_num) and (len(stack) == 0):
    for output in output_list:
        print(output)
else:
    print('NO')