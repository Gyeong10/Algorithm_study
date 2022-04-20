grid = [([0] * 1001) for _ in range(1001)]

case_num = int(input())
result = [0]*(case_num+1)

for test_case in range(1, case_num + 1):
    input_i, input_j, M, N = map(int, input().split())
    for i in range(input_i, input_i + M):
        for j in range(input_j, input_j + N):
            grid[i][j] = test_case

for i in range(1001):
    for j in range(1001):
        if grid[i][j]:
            result[grid[i][j]] += 1

for test_case in range(1, case_num+1):
    print(result[test_case])