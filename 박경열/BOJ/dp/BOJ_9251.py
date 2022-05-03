import sys; sys.stdin = open('BOJ_9251.txt')

strs1 = [''] + list(sys.stdin.readline().rstrip())
strs2 = [''] + list(sys.stdin.readline().rstrip())

arr = [[0] * len(strs2) for _ in range(len(strs1))]


for i in range(1, len(strs1)):
    for j in range(1, len(strs2)):
        if strs1[i] == strs2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[-1][-1])