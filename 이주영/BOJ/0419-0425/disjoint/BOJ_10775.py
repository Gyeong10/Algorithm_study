import sys


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(P)]
parent = [x for x in range(G+1)]
