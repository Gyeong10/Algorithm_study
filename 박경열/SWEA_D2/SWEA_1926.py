# D2 간단한 369게임

N = int(input())

clap = ['3', '6', '9']

for i in range(1, N+1):

    count = 0
    A = list(str(i))

    for j in range(len(A)):
        if A[j] in clap:
            count += 1

    if count == 0:
        print(i, end='')
    else:
        print('-' * count, end='')

    print(end=' ')