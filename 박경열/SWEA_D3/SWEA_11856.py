# D3 반반

T = int(input())

for tc in range(T):
    N = input()
    how = [0]*26

    for i in range(4):
        how[ord(N[i])-65] += 1

    cnt = 0
    for num in how:
        if num == 2:
            cnt += 1

    if cnt == 2:
        ans = 'Yes'
    else:
        ans = 'No'

    print(f'#{tc+1} {ans}')