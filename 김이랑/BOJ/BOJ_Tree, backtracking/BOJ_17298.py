N = int(input())
num_list = list(map(int, input().split()))

answer_list = [-1] * N
stack = []

for i in range(0, N):
    while stack and num_list[stack[-1]] < num_list[i]:
        answer_list[stack.pop()] = num_list[i]
    stack.append(i)

print(*answer_list)