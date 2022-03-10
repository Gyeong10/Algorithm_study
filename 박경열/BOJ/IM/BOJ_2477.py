# 참외밭

import sys

def solve(cnt, pear):
    for i in range(6):
        cnt[pear[i][0]] += 1
        if cnt[pear[i][0]] == 2:
            for j in range(6):
                if pear[i][0] == pear[j][0] and i - j != 4:
                    many = K * (pear[j - 1][1] * pear[j][1] + pear[i][1] * pear[i + 1][1])
                    return many
                elif pear[i][0] == pear[j][0] and j == 0 and i != 4:
                    many = K * (pear[5][1] * pear[j][1] + pear[i][1] * pear[i + 1][1])
                    return many
                elif pear[i][0] == pear[j][0] and i - j == 4:
                    many = K * (pear[j + 1][1] * pear[j][1] + pear[i][1] * pear[i - 1][1])
                    return many


K = int(sys.stdin.readline())

pear = []
cnt = [0]*5

for i in range(6):
    a, b = map(int, sys.stdin.readline().split())
    pear.append([a, b])

print(solve(cnt, pear))