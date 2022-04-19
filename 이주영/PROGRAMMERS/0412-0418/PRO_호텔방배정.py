# 정확 O, 효율 X
# def solution(k, room_number):
#     answer = []
#     visited = [0] * (k+1)
#     for room in room_number:
#         for i in range(room, k+1):
#             if not visited[i]:
#                 visited[i] = 1
#                 answer.append(i)
#                 break
#     return answer

def check(visited, rooms, room):
    t = 1
    while True:
        if not visited[rooms[room] + t]:
            # rooms[room] += (t + 1)
            break
        t += 1
    return t


def solution(k, room_number):
    answer = []
    rooms = [x for x in range(k+1)]
    visited = [0] * (k+1)
    for room in room_number:
        # 방사용 가능
        if not visited[room]:
            visited[room] = 1
            answer.append(room)
            rooms[room] += 1
        # 방사용 불가능 / rooms속 방 번호 > 원하는 방 번호
        elif rooms[room] > room:
            visited[rooms[room]] = 1
            answer.append(rooms[room])
            rooms[room] += check(visited, rooms, room)
            # t = 1
            # while True:
            #     if not visited[rooms[room] + t]:
            #         rooms[room] += (t + 1)
            #         break
            #     t += 1
        # rooms의 방번호 < 원하는 방번호
        elif rooms[room] < room:
            room += check(visited, rooms, room)
            visited[room] = 1
            answer.append(room)
            rooms[room] += check(visited, rooms, room)

    return answer

k = 10
r = [1,3,4,1,3,1]
print(solution(k, r))