C, R = map(int, input().split())
now_C, now_R = map(int, input().split())
check = int(input())
x = y = 1
count = 0

a = b = 0


def check_direction(now_C, now_R, x, y):
    if (now_C == 0 and now_R == 0) or (now_C == C and now_R == 0) or (now_C == 0 and now_R == R) or (now_C == C and now_R == R):
        return -x, -y
    elif now_C == C or now_C == 0:
        return -x, y
    elif now_R == R or now_R == 0:
        return x, -y
    else:
        return x, y


while count <= check:
    x, y = check_direction(now_C, now_R, x, y)
    if count == check:
        break
    while 0 <= now_C + x <= C and 0 <= now_R + y <= R:
        if count == check:
            break
        else:
            now_C += x
            now_R += y
            count += 1

print(now_C, now_R)