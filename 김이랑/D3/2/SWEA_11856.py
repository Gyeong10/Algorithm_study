import sys
sys.stdin = open('sample_input.txt', 'r')

case_num = int(input())
for test_case in range(1, case_num+1):
    words = input()
    word = []
    for string in words:
        word.append(string)
    answer = 'No'
    if word[0] == word[1]:
        if word[0] != word[2] == word[3]:
            answer = 'Yes'
    elif word[0] == word[2]:
        if word[0] != word[1] == word[3]:
            answer = 'Yes'
    elif word[0] == word[3]:
        if word[0] != word[1] == word[2]:
            answer = 'Yes'
    print(f"#{test_case} {answer}")



