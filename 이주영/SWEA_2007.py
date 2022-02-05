T = int(input())
for t in range(1, T+1):
    long_str = input()
    for i in range(1, 11):
        if long_str[:i] == long_str[i:2*i]:
            print(f'#{t} {i}')
            break