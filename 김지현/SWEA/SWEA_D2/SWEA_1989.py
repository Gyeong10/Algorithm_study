tests = int(input())

for t in range(1,tests+1):
    word = input()
    for w in range(len(word)//2):
        if word[w] != word[len(word)-w-1]:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')        


# if word == word[::-1]:
#     print(f'#{t} 1')
# else :
#     print(f'#{t} 0')

