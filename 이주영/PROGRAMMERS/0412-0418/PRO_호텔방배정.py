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

import sys
sys.setrecursionlimit(10**4)

def check(rooms, number):
    if number in rooms:
        room = check(rooms, rooms[number])
        rooms[number] = room + 1
        return room
    else:
        rooms[number] = number + 1
        return number


def solution(k, room_number):
    answer = []
    rooms = {}
    for number in room_number:
        room = check(rooms, number)
        answer.append(room)
    return answer

k = 10
r = [1,3,4,1,3,1]
print(solution(k, r))