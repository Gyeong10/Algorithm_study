import sys
sys.setrecursionlimit(10000)

def check(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    else:
        room = check(rooms[number], rooms)
        rooms[number] = room + 1
        return room

def solution(k, room_number):
    answer = []
    rooms = dict()

    for number in room_number:
        room = check(number, rooms)
        answer.append(room)
    return answer

arr = [1,3,4,1,3,1]
print(solution(10, arr))