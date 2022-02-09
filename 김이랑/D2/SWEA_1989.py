test_num = int(input())
for test_case in range(1, test_num + 1):
    word = input()
    word_len = len(word)
    #tomato
    #level
    for i in range(word_len//2): #2까지
        if word[i] != word[word_len-1-i]:
            print(f'#{test_case} 0')
            break
    else :
        print(f'#{test_case} 1')