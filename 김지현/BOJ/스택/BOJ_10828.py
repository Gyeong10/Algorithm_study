import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    
    elif s[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
