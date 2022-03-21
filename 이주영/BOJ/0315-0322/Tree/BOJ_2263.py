import sys
sys.setrecursionlimit(10**6) # 재귀 호출 에러 방지
# 전위 순회
def pre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    parent = post_arr[post_end]
    print(parent, end=' ')

    left = arr[parent] - in_start
    right = in_end - arr[parent]

    pre(in_start, in_start+left-1, post_start, post_start+left-1)   # 왼쪽
    pre(in_end-right+1, in_end, post_end-right, post_end-1)         # 오른쪽


N = int(input())
in_arr = list(map(int, input().split()))
post_arr = list(map(int, input().split()))
arr = [0] * (N+1)
# 인오더 정점번호들을 인덱스로 저장
for i in range(N):
    arr[in_arr[i]] = i
pre(0, N-1, 0, N-1)
