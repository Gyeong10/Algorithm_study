# 별 > 동그라미 > 네모 > 세모
def card(num, arr):
    cnt = [0]*5
    for i in range(num):
        cnt[arr[i]] += 1
    return cnt

n = int(input())
for _ in range(n):
    a_n, *a = map(int, input().split())
    b_n, *b = map(int, input().split())
    #모양 수세기
    card_a = card(a_n, a)
    card_b = card(b_n, b)
    #모양 갯수비교
    ans = ''
    for i in range(4,0,-1):
        if card_a[i] > card_b[i]:
            ans = 'A'
            break
        elif card_a[i] < card_b[i]:
            ans = 'B'
            break
    if ans == '':
        ans = 'D'
    print(ans)
        