# D2 패턴 마디의 길이

T = int(input())

for i in range(T):
    words = input()

    for j in range(10):
        if words[0 : j+1] == words[j+1 : j*2 + 2]:
            print(f'#{i+1} {j+1}')
            break