# 요상한 사전
# p문자열에 마지막에 'a'가 더 적혀있는 문자열이 q인 경우 말고는 모두 Y 출력
T = int(input())
for t in range(1, T+1):
    p = input().rstrip()
    q = input().rstrip()
    if p + 'a' == q:
        print(f'#{t} N')
    else:
        print(f'#{t} Y')
