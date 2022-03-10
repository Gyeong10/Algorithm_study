n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
updown = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
max_total = 0
for i in range(n):
    squares = []
    jusawi = [1, 2, 3, 4, 5, 6]
    jusawi.remove(arr[0][i])
    next = arr[0][updown[i]]
    jusawi.remove(next)
    squares.append(max(jusawi))
    for j in range(1, n):
        jusawi = [1, 2, 3, 4, 5, 6]
        jusawi.remove(next)
        next = arr[j][updown[arr[j].index(next)]]
        jusawi.remove(next)
        squares.append(max(jusawi))
    result = sum(squares)
    if max_total < result:
        max_total = result
print(max_total)