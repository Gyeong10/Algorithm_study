# 두개의 문자가 두개씩 있는지 여부
T = int(input())
arr = [input() for _ in range(T)]
# 1. alphabet 사용
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
# for t in range(T):
#     cnt = [0] * 26
#     al_cnt = 0
#     for i in range(4):
#         for j in range(26):
#             if arr[t][i] == alphabet[j]:
#                 cnt[j] += 1
#                 break
#     for i in range(26):
#         if cnt[i] == 2:
#             al_cnt += 1
#     if al_cnt == 2:
#         print(f'#{t+1} Yes')
#     else:
#         print(f'#{t+1} No')
# 2. 본인부터 마지막 인덱스까지 본인과 같은 값이면 cnt에 1 더해주고,
# cnt가 2면 al_cnt에 1 더해주고, al_cnt가 2이면 Yes 출력, 아니면 No 출력
for t in range(T):
    al_cnt = 0
    for i in range(4):
        cnt = 0
        for j in range(i, 4):
            if arr[t][i] == arr[t][j]:
                cnt += 1
        if cnt == 2:
            al_cnt += 1
    if al_cnt == 2:
        print(f'#{t+1} Yes')
    else:
        print(f'#{t+1} No')