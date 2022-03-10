# 9012 괄호
import sys

def compare(VPS):
    stack = []

    for V in VPS:
        if V == '(':
            stack.append(V)
        else:
            if not stack:
                return 'NO'
            elif stack[-1] == '(':
                stack.pop()

    if stack:
        return 'NO'
    else:
        return 'YES'


T = int(sys.stdin.readline())

for _ in range(T):
    VPS = list(sys.stdin.readline())
    VPS = VPS[:-1]

    ans = compare(VPS)
    print(ans)