T = int(input())
arr = [list(input()) for _ in range(T)]
for t in range(T):
    max = int(''.join(arr[t]))
    min = int(''.join(arr[t]))
    for x in range(len(arr[t])-1):
        for y in range(x+1, len(arr[t])):
            if arr[t][y] == '0' and x == 0:
                continue
            arr[t][x], arr[t][y] = arr[t][y], arr[t][x]
            change = int(''.join(arr[t]))
            max = change if max < change else max
            min = change if min > change else min
            arr[t][x], arr[t][y] = arr[t][y], arr[t][x]
    print(f'#{t+1} {min} {max}')

