height = []
two_total = -100
for i in range(9):
    num = int(input())
    two_total += num
    height.append(num)

# 아 솔트 함수 쓰게 해줘용
height.sort()

# 빠지는거 두개 찾기
remove_1 = -1
remove_2 = -1
for i in range(9):
    for j in range(9):
        if two_total == height[i] + height[j]:
            if i != j:
                remove_1 = height[i]
                remove_2 = height[j]

for i in range(9):
    if height[i] == remove_1 or height[i] == remove_2:
        continue
    print(height[i])