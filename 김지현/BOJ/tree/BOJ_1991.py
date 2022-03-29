import sys
def pre_order(n):
    if n <= N:
        print(chr(n-1+ord('A')), end='')
        if left[n]:
            pre_order(left[n])
        if right[n]:
            pre_order(right[n])


def in_order(n):
    if n <= N:
        if left[n]:
            in_order(left[n])
        print(chr(n - 1 + ord('A')), end='')
        if right[n]:
            in_order(right[n])

def post_order(n):
    if n <= N:
        if left[n]:
            post_order(left[n])
        if right[n]:
            post_order(right[n])
        print(chr(n - 1 + ord('A')), end='')


N = int(sys.stdin.readline())
left = ['']*(N+1)
right = ['']*(N+1)
for _ in range(N):
    temp = list(sys.stdin.readline().split())
    i = ord(temp[0]) - ord('A') + 1
    if temp[1] != '.':
        left[i] = ord(temp[1]) - ord('A') +1
    if temp[2] != '.':
        right[i] = ord(temp[2]) - ord('A') +1

pre_order(1)
print()
in_order(1)
print()
post_order(1)