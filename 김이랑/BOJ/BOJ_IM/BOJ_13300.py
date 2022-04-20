N, K = map(int, input().split())

# 각 학년 담을 배열
girls = [0] * 7
boys = [0] * 7

# 입력받기, 학생수만큼 돌면서 성별맞춰서 넣어주기
for i in range(N):
    S, Y = map(int, input().split())
    if S:
        girls[Y] += 1
    else:
        boys[Y] += 1

#받은거 나누기
room = 0
for i in range(7):
    # 나머지 있으면 방하나 추가하고, 없으면 그냥 몫만! 0도 자연스럽게 걸러짐
    if girls[i] % K:
        room += (girls[i] // K + 1)
    else:
        room += girls[i] // K

    if boys[i] % K:
        room += (boys[i] // K + 1)
    else:
        room += boys[i] // K

print(room)