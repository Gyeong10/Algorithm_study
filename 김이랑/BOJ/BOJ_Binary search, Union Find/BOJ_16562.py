N, M, k = map(int, input().split())
friend_fee = [0] + list(map(int, input().split()))
parent = list(range(N+1))


def get_parent(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = get_parent(parent[a])
        return parent[a]


def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    # 친구비로 유니언 하기
    if friend_fee[parent_a] <= friend_fee[parent_b]:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


for i in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 다시 부모 다 세팅하기
for i in range(N+1):
    get_parent(i)

parent = list(set(parent))

need_money = 0
for i in range(len(parent)):
    need_money += friend_fee[parent[i]]

if need_money > k:
    print('Oh no')
else:
    print(need_money)