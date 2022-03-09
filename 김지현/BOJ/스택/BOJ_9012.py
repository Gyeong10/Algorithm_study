import sys
T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break
    
    if stack:
        print('NO')
    else:
        print('YES')