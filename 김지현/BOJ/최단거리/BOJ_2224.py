import sys

input = sys.stdin.readline
INF = int(1e9)

graph = [[INF] * (52) for _ in range(52)]

for _ in range(int(input())):
    a, b, c = input().split()

    a_ord = ord(a)
    c_ord = ord(c)

    if a_ord >= ord('a'):
        a_ord = a_ord - (ord('a') - ord('Z') - 1)
    if c_ord >= ord('a'):
        c_ord = c_ord - (ord('a') - ord('Z') - 1)

    a_ord = a_ord - ord('A')
    c_ord = c_ord - ord('A')

    graph[a_ord][c_ord] = 1

for a in range(52):
    for b in range(52):
        if a == b:
            graph[a][b] = 0

for k in range(52):
    for a in range(52):
        for b in range(52):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

arr = []
for a in range(52):
    for b in range(52):
        if graph[a][b] == 0 or graph[a][b] == 1e9:
            pass
        else:
            arr.append(a)
            arr.append(b)


print(len(arr) // 2)
for i in range(0, len(arr), 2):
    a = arr[i]
    c = arr[i + 1]

    if a > 25:
        a = a + (ord('a') - ord('Z') - 1)
    if c > 25:
        c = c + (ord('a') - ord('Z') - 1)
    a = a + ord('A')
    c = c + ord('A')
    print("%c => %c" % (chr(a), chr(c)))