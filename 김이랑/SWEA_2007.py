import sys
sys.stdin = open("input (2).txt", "r")

test_num = int(input())

for i in range(1, test_num + 1):
    words = input()
    len = 0

# sumsumpam 이면 예외될거같기도 함
    for j in range(1, 11):
        new_word = words[0:j]
        test_word = words[j:(j+j)]
        if new_word == test_word:
            len = j
            break

    print(f'#{i} {len}')





