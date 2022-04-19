# 1. 정확 100 효율 0
# def solution(stones, k):
#     answer = 0
#     stones.append(200000000)
#     while True:
#         flag = 0
#         stone = -1
#         while stone < len(stones)-2:
#             stone += 1
#             if stones[stone]:
#                 stones[stone] -= 1
#             else:
#                 for i in range(1, k):
#                     if stone + i < len(stones) and stones[stone+i]:
#                         stone += i
#                         stones[stone] -= 1
#                         break
#                 else:
#                     flag = 1
#         if flag:
#             break
#         answer += 1
#     return answer


def solution(stones, k):
    left = 1
    right = 200_000_000
    while left <= right:
        tmp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in tmp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left


s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(s, k))