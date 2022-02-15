import sys
sys.stdin = open("sample_input.txt", "r")case_num = int(input())
for test_case in range(1, case_num+1):
    num_num = int(input())
    nums = list(map(int, input().split()))
    answer = 0
    for i in range(1, len(nums)-1):
        if nums[i+1] > nums[i] > nums[i-1]:
            answer += 1
        elif nums[i+1] < nums[i] < nums[i-1]:
            answer += 1

    print(f"#{test_case} {answer}")

