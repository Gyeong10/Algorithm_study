# 1991 트리 순회

import sys

sys.stdin = open('BOJ_1991.txt')

def perorder(v):
    global s1

    if v:
        s1 += chr(v + 64)
        perorder(c1[v])
        perorder(c2[v])
    return


def inorder(v):
    global s2

    if v:
        inorder(c1[v])
        s2 += chr(v + 64)
        inorder(c2[v])
    return


def postorder(v):
    global s3

    if v:
        postorder(c1[v])
        postorder(c2[v])
        s3 += chr(v + 64)
    return


N = int(sys.stdin.readline())
c1 = [0] * (N + 1)
c2 = [0] * (N + 1)

for i in range(N):
    a, b, c = map(str, sys.stdin.readline().split())

    if b != '.':
        c1[ord(a)-64] = ord(b)-64
    if c != '.':
        c2[ord(a)-64] = ord(c)-64

s1 = ''
s2 = ''
s3 = ''

perorder(1)
inorder(1)
postorder(1)

print(s1)
print(s2)
print(s3)