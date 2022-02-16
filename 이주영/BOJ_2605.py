# 줄세우기

# 문제에 나온 대로 하나씩 넣으면서 자리 찾아 넣었음
# 값이 안 들어 있으면 바로 넣고
# 값이 있으면 그 자리 수부터 뒷 자리 숫자 모두 한 칸씩 미루고 넣기

N = int(input())
arr = list(map(int, input().split()))

result = [0] * N
for i in range(N):
    if result[i-arr[i]] == 0:
        result[i-arr[i]] = i+1
    else:
        for j in range(N-1, i-arr[i]-1, -1):
            if result[j] != 0:
                result[j+1] = result[j]
        result[i-arr[i]] = i+1
print(*result)


# 뒤에서부터 swap하면서 풀려고 했는데 안되는 방법 같아여,,
# result = [x for x in range(1, N+1)]
# for i in range(N-1, N//2 -1, -1):
#     for j in range(N):
#         if result[j] == i+1:
#             idx = j
#             break
#     if result[idx-arr[i]] == i+1:
#         continue
#     else:
#         result[idx], result[idx-arr[i]] = result[idx-arr[i]], result[idx]
# print(result)

