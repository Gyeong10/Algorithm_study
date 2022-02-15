import sys
sys.stdin = open("sample_input.txt", "r")

case_num = int(input())
result = []
for test_case in range(1, case_num+1):
    prev_word = input().strip()
    next_word = input().strip()

    answer = 'Y'
    # 길이가 하나 차이날 때
    if len(next_word) - len(prev_word) == 1:
        if prev_word == next_word[0:-1]:
            if next_word[-1] == 'a':
                answer = 'N'

    # 같을때
    elif next_word == prev_word:
        answer = 'N'

    # 길이가 같을때
    # elif len(next_word) == len(prev_word):
    #     same = 1
    #     for i in range(0, len(next_word)-1):
    #         if prev_word[i] != next_word[i]:
    #             same = 0
    #     if same == 1:
    #         if ord(next_word[-1]) - ord(prev_word[-1]) == 1:
    #             answer = 'N'
    #
    # elif len(prev_word) == 10 and len(next_word) == 1:
    #     same = 1
    #     for i in range(1, len(prev_word)):
    #         if prev_word[i] != 'z':
    #             same = 0
    #     if same == 1:
    #         if ord(next_word[0]) - ord(prev_word[0]) == 1:
    #             answer = 'N'

    result.append(answer)

for test_case in range(case_num):
    print(f"#{test_case + 1} {result[test_case]}")
