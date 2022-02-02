import sys
sys.stdin = open("input (2).txt", "r")

test_num = int(input())

for i in range(1, test_num + 1):
    case_list_len = int(input())
    case_list = list(map(int, input().split()))

    max_idx = []

    for j in range(1, case_list_len):
        # 마지막이 클 경우, 마지막 추가
        if (j == case_list_len-1) and (case_list[j] > case_list[j-1]):
            max_idx.append(j)
        # 마지막이 안클 경우 그냥 끝
        elif (j == case_list_len-1):
            continue
    # 끝까지 돌았는데 max가 없을때, 첫번째 거 추가
        elif (j == case_list_len-1) and (len(max_idx) == 0):
            max_idx.append(0)
        # 전거보다 크고, 다음거보다 클 때 추가
        elif case_list[j] > case_list[j+1] and case_list[j] > case_list[j-1]:
            max_idx.append(j)

    answer = 0
    # 3, 5, 9 [2]
    # 1,1,3,1,2 [2,4] = [2, 4]
    # 1,1,3,1,4,5,3, 7 [2,4,5 7] = [7]

    new_idx = []

    for j in range(len(max_idx)-1):
        max = j
        for k in range(j, len(max_idx)-1):
            if case_list[max] < case_list[max_idx[k]]:
                max = k
        if max == j:
         new_idx.append(max_idx[j])

    new_idx.append(max_idx[-1])

    for j in range(len(new_idx)):
       # 첫번째 꺼가 최대일 때
       if new_idx[j] == 0:
           answer = 0
        # 끝에가 최대일때
       elif new_idx[j] == (case_list_len - 1):
           for k in range(j, new_idx[j]):
               if case_list[new_idx[j]] > case_list[k]:
                   answer = case_list[new_idx[j]] - case_list[k] + answer
       # 첫번째 인덱스 까지
       elif  j == 0 :
           for k in range(j, new_idx[j]):
               if case_list[new_idx[j]] > case_list[k]:
                   answer = case_list[new_idx[j]] - case_list[k] + answer
       # 사이 인덱스들..
       else:
           for k in range(new_idx[j-1], new_idx[j]):
               if case_list[new_idx[j]] > case_list[k]:
                   answer = case_list[new_idx[j]] - case_list[k] + answer


    print(f'#{i} {answer}')




