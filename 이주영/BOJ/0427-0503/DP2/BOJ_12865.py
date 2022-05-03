# 1) x축엔 가방 1~K까지의 무게, y축은 물건N개 개수만큼의 배열을 만들어준다.
# 2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.
# 3 - 0) 현재물건이 현재 돌고있는 무게보다 작다면 바로 [이전물건][같은 무게](knapsack[i - 1][j])를 입력
# 3 - 1) 현재물 건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i - 1][j - weight])을 위의 행에서 가져와 더해준다.
# 3 - 2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는값(knapsack[i - 1][j])을 가져온다.
# 4) 3 - 1과 3 - 2 중 더 큰 값을 knapsack[i][j]에 저장해준다.이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성
# 5) knapsack[N][K] 는 곧, K무게일 때의 최댓값을 가리킨다.

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < arr[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(arr[i][1] + dp[i-1][j-arr[i][0]], dp[i-1][j])
print(dp[N][K])

