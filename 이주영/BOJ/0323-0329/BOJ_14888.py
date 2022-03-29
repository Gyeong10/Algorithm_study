def cal(n1, n2, ch):
    if ch == 0:
        return n1 + n2
    elif ch == 1:
        return n1 - n2
    elif ch == 2:
        return n1 * n2
    else:
        if n1 * n2 < 0:
            return -(abs(n1) // abs(n2))
        else:
            return n1 // n2


def solve(caled, idx):
    global max_value, min_value
    if idx == N:
        if max_value < caled:
            max_value = caled
        if min_value > caled:
            min_value = caled
        return
    for k in range(4):
        if oper[k]:
            oper[k] -= 1
            solve(cal(caled, nums[idx], k), idx+1)
            oper[k] += 1



max_value, min_value = -(10**10), 10**10
N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))  # [ +개수, -개수, *개수, //개수]
solve(nums[0], 1)
print(max_value, min_value, sep='\n')