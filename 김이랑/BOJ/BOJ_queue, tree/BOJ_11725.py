N = int(input())
# 왼, 오, 부모
tree_child = [[0] for _ in range(N+1)]
tree_parent = [0, -1] + [0] * (N-1)

for i in range(N-1):
    v1, v2 = map(int, input().split())
    if tree_parent[v1]:
        tree_child[v1].append(v2)
        tree_parent[v2] = v1
    elif tree_parent[v2]:
        tree_child[v2].append(v1)
        tree_parent[v1] = v2

check_parent = tree_parent[2:]

for v in check_parent:
    if v:
        print(v)