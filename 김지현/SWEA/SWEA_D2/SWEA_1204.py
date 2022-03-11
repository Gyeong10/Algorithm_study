import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    n = int(input())
    score = list(map(int, input().split()))
    count = [0] * 101

    for i in score:
        count[i] += 1

    max_idx = 0
    for i in range(101):
        if count[i] >= count[max_idx]:
            max_idx = i
        
    print(f'#{n} {max_idx}')