T = int(input())

for t in range(1, T+1):
    S = input()
    cnt = [0] * 26

    for i in S:
        cnt[ord(i)-65] += 1

    ans = 0
    for i in range(26):
        if cnt[i] == 2:
            ans += 1
    if ans == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')    