import sys; sys.stdin = open('BOJ_20164.txt')

def plus(arr):
    s = ''
    for a in arr:
        s += str(a)
    return int(s)


def solve(n, temp):
    global ans

    nums = list(map(int, n))
    for num in nums:
        if num % 2:
            temp += 1

    if len(nums) == 1:
        if temp > ans[0]:
            ans[0] = temp

        if temp < ans[1]:
            ans[1] = temp
        return

    if len(nums) == 2:
        solve(str(nums[0] + nums[1]), temp)

    if len(nums) >= 3:
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                num1 = nums[:i+1]
                num2 = nums[i+1:j+1]
                num3 = nums[j+1:]
                solve(str(plus(num1) + plus(num2) + plus(num3)), temp)


N = sys.stdin.readline().rstrip()
ans = [0, 10**9]
solve(N, 0)
print(ans[1], ans[0])