import sys
sys.stdin = open("sample_input.txt", "r")

case_num = int(input())

for test_case in range(1, case_num+1):
    nums = input()
    # 제일 큰거 : 첫자리와 젤 큰수 바꾸는거
    # 9 면 다음거하고 바꾸면됨
    max_replace_idx = 0
    max_idx = 0
    for i in range(len(nums)):
        #99990 일경우 비교해봐야함
        if max_replace_idx == len(nums) - 2:
            if nums[len(nums) - 2] > nums[len(nums) - 1]:
                max_replace_idx, max_idx = len(nums) - 1, len(nums) - 2
        # 바꿀숫자가 9일경우 그다음거로 바꾸기
        elif int(nums[max_replace_idx]) == 9:
            max_replace_idx =  i+1
            max_idx = i+1
        # 나머지는 걍 가기
        else:
            for j in range(i, len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            break

    # 리플레이스 와 최대 값과 같을때, -> max인덱스 다음과 왼쪽에서 거기 인덱스 찾기
    if nums[max_replace_idx] == nums[max_idx]:
        if max_replace_idx != len(nums) - 1:
            for i in range (len(nums)):
                if nums[i] == nums[max_replace_idx]:
                    max_idx = i
            max_replace_idx = max_replace_idx + 1

    min_replace_idx = 0
    min_idx = 0
    # 첫자리 1이면 인덱스 한차례 옮기기
    if int(nums[min_replace_idx]) == 1:
        min_replace_idx =  1
        min_idx = 1

    # 젤 작은거 : 첫자리랑 젤 작은수 바꾸는거
    # 다음자리 0이면 다음으로 넘어가기
    # 10101 경우 비교해봐야함
    for i in range(min_replace_idx, len(nums)):
        if min_replace_idx == len(nums) - 2:
            if nums[len(nums) - 2] < nums[len(nums) - 1]:
                min_replace_idx, min_idx = len(nums) - 1, len(nums) - 2
        elif int(nums[min_replace_idx]) == 0:
            min_replace_idx =  i+1
            min_idx = i+1
        else:
            for j in range(min_replace_idx, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            break

    #0 1
    #20202만 해결하면 끝일듯 ㅡㅡ
    # 포문 돌았는데 min_replace idx가 0이 아닌 가장 작은 ㅇ값일 경우 민 인덱스 플러스 1
    min_not_zero = min_replace_idx
    for i in range(min_replace_idx, len(nums)):
        if (int(nums[min_not_zero]) < int(nums[i])) and (int(nums[i]) != 0):
            min_not_zero = i

    for i in range(min_replace_idx, len(nums)):
        if int(nums[min_replace_idx]) == 0:
           if min_replace_idx != len(nums)-1:
               min_replace_idx = min_replace_idx + 1

    if nums[min_not_zero] == nums[min_replace_idx] and min_replace_idx != len(nums)-1:
        min_replace_idx = min_replace_idx + 1


    print(max_replace_idx, max_idx)
    print(min_replace_idx, min_idx)

    #숫자 바꾸기
    num_list = []
    for num in nums:
        num_list.append(str(num))

    max_list = list(num_list)
    max_replace_num = num_list[max_replace_idx]
    max = num_list[max_idx]

    max_list[max_replace_idx] = max
    max_list[max_idx] = max_replace_num
    answer_max = ''.join(max_list)

    min_list = list(num_list)
    min_replace_num = num_list[min_replace_idx]
    min = num_list[min_idx]

    min_list[min_replace_idx] = min
    min_list[min_idx] = min_replace_num
    answer_min = ''.join(min_list)

    print(f"#{test_case} {answer_min} {answer_max}")
