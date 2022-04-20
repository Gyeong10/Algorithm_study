N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

oper_N = sum(operators)
operators = ['+'*operators[0] + '-'*operators[1] + '*'*operators[2] + '/'*operators[3]]
temp = operators.pop()

for i in range(len(temp)):
    operators.append(temp[i])

visited = [False]*oper_N
order = ['']*oper_N


def dfs(D):
    global min_total, max_total

    if D == oper_N:
        total = nums[0]
        for i in range(oper_N):
            if order[i] == '+':
                total = total + nums[i+1]
            elif order[i] == '-':
                total = total - nums[i+1]
            elif order[i] == '*':
                total = total * nums[i+1]
            elif order[i] == '/':
                total = int(total / nums[i+1])
        if total > max_total:
            max_total = total
        if total < min_total:
            min_total = total

    for i in range(oper_N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            order[D] = operators[i]
            dfs(D+1)
            visited[i] = False


min_total = 1000000001
max_total = -1000000001

dfs(0)

print(max_total)
print(min_total)