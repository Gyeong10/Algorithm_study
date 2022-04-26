N = int(input())
num = list(map(int, input().split()))

num.sort()
max_idx = N-1
min_idx = 0

value = abs(num[min_idx] + num[max_idx])
answer = [num[min_idx], num[max_idx]]

while min_idx < max_idx:
    temp = num[min_idx] + num[max_idx]
    if temp == 0:
        answer[0] = num[min_idx]
        answer[1] = num[max_idx]
        break
    elif temp < 0:
        if abs(temp) < value:
            value = abs(temp)
            answer[0] = num[min_idx]
            answer[1] = num[max_idx]
        min_idx += 1
    elif temp > 0:
        if abs(temp) < value:
            value = abs(temp)
            answer[0] = num[min_idx]
            answer[1] = num[max_idx]
        max_idx -= 1

print(*answer)