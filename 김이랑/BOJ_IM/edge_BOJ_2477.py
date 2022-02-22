melon = int(input())

direction = []
distance = []

for _ in range(6):
    dir, dis = map(int, input().split())
    direction.append(dir)
    distance.append(dis)

direction += direction
distance += distance

idx = 0
for i in range(10):
    if direction[i] == direction[i+2]:
        idx = i
        break

# 엥 반례가 있나요??? 왜?? 완벽한데??
area = (distance[idx+4] * distance[idx+5]) - (distance[idx+1] * distance[idx+2])
print(area*melon)