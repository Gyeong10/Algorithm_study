n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n - 1
answer = 2e+9+1
result = []
while left < right:
    l_left = arr[left]
    l_right = arr[right]

    total = l_left + l_right
    if abs(total) < answer:
        answer = abs(total)
        result = [l_left, l_right]

    if total < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
