# 오 아예 모르겠는걸요?
N = int(input())

tree = [[] for _ in range(N+1)]
in_order_list = list(map(int, input().split()))
post_order_list = list(map(int, input().split()))

