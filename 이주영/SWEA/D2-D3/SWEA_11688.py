# Calkin-Wilf tree 1
T = int(input())
arr = [input() for _ in range(T)]
# 1.
# for t in range(T):
#     root = [1, 1]
#     for i in range(len(arr[t])):
#         if arr[t][i] == 'L':
#             root[1] += root[0]
#         else:
#             root[0] += root[1]
#     for i in range(2, int((len(arr[t])+1) ** 0.5)):
#         if root[0] % i == 0 and root[1] % i == 0:
#             root %= i
#     print(f'#{t+1}', end=' ')
#     print(*root)

# 2.
for t in range(T):
    