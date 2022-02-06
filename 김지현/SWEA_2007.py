tests = int(input())

for t in range(1,tests+1):
    words = input()
    for i in range(1,len(words)+1):
        if words[:i] == words[i:2*i]:
            print(f'#{t} {i}')
            break