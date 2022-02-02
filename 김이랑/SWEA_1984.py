test_num = int(input())
# 이것도 굳이 풀이할 필요 있을까
# O(2n)이면 o(n) 아닌가? 이거보다 더 빠르게 하는 방법이 있을라나
for case_num in range(1, test_num + 1):
    num_list = list(map(int, input().split()))
    min = num_list[0]
    max = num_list[0]
    for num in num_list:
        if min > num:
            min = num
        elif max < num:
            max = num
    sum = 0
    for num in num_list:
        if (num != min) and (num != max):
            sum = sum + num

    # 파이썬 라운드 함수가 좀 꼬롬하긴해
    ave = round(sum/(len(num_list)-2))

    print(f'#{case_num} {ave}')
