import sys; sys.stdin = open('BOJ_2470.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0
end = N - 1
ans = [arr[0], arr[-1]]

while start < end:
    if not abs(sum(ans)):
        break

    minus = abs(arr[start] + arr[end])

    if start + 1 < end and abs(arr[start + 1] + arr[end]) < minus:
        start += 1
    elif start < end - 1 and abs(arr[start] + arr[end - 1]) < minus:
        end -= 1
    else:
        if minus < abs(sum(ans)):
            ans = [arr[start], arr[end]]
        start += 1
        end -= 1

print(*ans)
