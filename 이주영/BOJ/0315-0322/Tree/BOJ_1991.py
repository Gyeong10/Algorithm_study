import sys

def preorder(n):
    print(chr(n-1 + ord('A')), end='')
    if tree[0][n]:
        preorder(tree[0][n])
    if tree[1][n]:
        preorder(tree[1][n])


def inorder(n):
    if tree[0][n]:
        inorder(tree[0][n])
    print(chr(n - 1 + ord('A')), end='')
    if tree[1][n]:
        inorder(tree[1][n])


def postorder(n):
    if tree[0][n]:
        postorder(tree[0][n])
    if tree[1][n]:
        postorder(tree[1][n])
    print(chr(n - 1 + ord('A')), end='')


N = int(sys.stdin.readline())
tree = [[''] * (N+1) for _ in range(2)]
for i in range(N):
    a, b, c = sys.stdin.readline().split()
    a = ord(a) - ord('A') + 1
    if b != '.':
        b = ord(b) - ord('A') + 1
        tree[0][a] = b
    if c != '.':
        c = ord(c) - ord('A') + 1
        tree[1][a] = c


preorder(1)
print()
inorder(1)
print()
postorder(1)