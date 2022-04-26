import sys; sys.stdin = open('BOJ_20444.txt')

def search():
    start = 0
    end = n

    while start < end:

        middle = start + (end - start) // 2
        cut = (middle + 1) * (n - middle + 1)

        if k == cut:
            return 'YES'

        elif cut < k:
            start = middle + 1

        else:
            end = middle

    return 'NO'


n, k = map(int, sys.stdin.readline().split())
print(search())