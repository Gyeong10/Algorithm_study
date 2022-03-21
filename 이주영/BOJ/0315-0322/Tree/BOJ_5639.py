import sys
sys.setrecursionlimit(10**5)    # 재귀 호출 에러 방지

def post_order(start, end):     # start: 시작 인덱스 end: 끝 인덱스
    if start > end:
        return
    cut = end + 1
    for i in range(start+1, end+1):
        if pre_tree[start] < pre_tree[i]:   # 크면 오른쪽 서브트리
            cut = i
            break

    post_order(start+1, cut-1)  # 왼쪽 서브트리
    post_order(cut, end)        # 오른쪽 서브트리
    print(pre_tree[start])


pre_tree = []
cnt = 0
# 들어오는 만큼 받기
while cnt <= 10000:
    try:
        tmp = int(sys.stdin.readline())
    except:
        break
    pre_tree.append(tmp)
    cnt += 1
post_order(0, cnt-1)