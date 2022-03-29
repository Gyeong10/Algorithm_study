N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

visited = [False]*N
all = list(range(N))
arr1 = [0]*(N//2)


def calculate(arr):
    total = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            total += grid[arr[i]][arr[j]] + grid[arr[j]][arr[i]]
    return total


def divide(start, D):
    global answer
    if D == N//2:
        arr2 = list(set(all) - set(arr1))
        temp1 = calculate(arr1)
        temp2 = calculate(arr2)
        if abs(temp1-temp2) < answer:
            answer = abs(temp1-temp2)

    else:
        for i in range(start, N):
            if not visited[i]:
                visited[i] = True
                arr1[D] = i
                divide(i, D+1)
                visited[i] = False

answer = 100000000
divide(0, 0)
print(answer)