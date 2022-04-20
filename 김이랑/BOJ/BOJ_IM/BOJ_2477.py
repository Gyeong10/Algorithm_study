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
    if direction[i] == direction[i+2] and direction[i+1] == direction[i+3]:
        idx = i
        break

area = (distance[idx+4] * distance[idx+5]) - (distance[idx+1] * distance[idx+2])
print(area*melon)