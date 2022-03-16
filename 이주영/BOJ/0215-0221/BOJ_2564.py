# 경비원
w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n+1)]
# (0,0)에서부터의 거리를 저장(무조건 시계방향으로의 거리)
course = []
for store in arr:
    if store[0] == 1:
        course.append(store[1] + h)
    elif store[0] == 2:
        course.append(2*h + w + (w-store[1]))
    elif store[0] == 3:
        course.append(h - store[1])
    else:
        course.append(h + w + store[1])
total = 0
# course_l : 시계방향으로의 거리, course_r : 반시계방향으로의 거리
for k in range(n):
    course_l = abs(course[-1] - course[k])
    course_r = 2 * (w+h) - course_l
    total += min(course_l, course_r)
print(total)
