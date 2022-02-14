T = int(input())

for t in range(1, T+1):
    A, B = map(int, input().split())

    if A + B >= 48:
        hour = A + B - 48
    elif A + B >= 24:
        hour = A + B - 24    
    else:
        hour = A + B

    print(f'#{t} {hour}')