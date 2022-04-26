N, M = map(int, input().split())
time_list = []
for i in range(N):
    time_list.append(int(input()))
time_list.sort()

min_time = time_list[0]
max_time = time_list[-1] * M


def check(mid):
    person = 0
    for time in time_list:
        person += (mid // time)
        if person >= M:
            return True
    return False

while min_time <= max_time:
    mid = (min_time + max_time)//2
    answer = mid
    if check(mid):
        max_time = mid - 1
    else:
        min_time = mid + 1

print((min_time+max_time)//2+1)