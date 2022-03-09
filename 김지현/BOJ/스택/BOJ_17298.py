import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1]*N
stack = [0]

for i in range(1,N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)


# 시간초과
# for i in range(N):
#     flag = 1
#     for j in range(i+1, N):
#         if A[j] > A[i]:
#             NGE.append(A[j])
#             flag = 0
#             break
#     if flag:
#         NGE.append(-1)