# 리스트 형태로 돌아옴
def get_parent(a):
    if a == relations[a][0]:
        return a
    else:
        relations[a][0] = get_parent(relations[a][0])
        return relations[a][0]

def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    if parent_a != parent_b:
        if relations[parent_a][1] < relations[parent_b][1]:
            relations[parent_a][0] = parent_b
            relations[parent_b][1] += relations[parent_a][1]
            relations[parent_a][1] = 0
            return relations[parent_b][1]
        else:
            relations[parent_b][0] = parent_a
            relations[parent_a][1] += relations[parent_b][1]
            relations[parent_b][1] = 0
            return relations[parent_a][1]
    else:
        return max(relations[parent_a][1], relations[parent_b][1])


for tc in range(int(input())):
    relations = {}
    F = int(input())
    for i in range(F):
        a, b = map(str, input().split())
        relation_a = relations.get(a, 0)
        if not relation_a:
            relations[a] = [a, 1]
        relation_b = relations.get(b, 0)
        if not relation_b:
            relations[b] = [b, 1]
        print(union(a, b))

