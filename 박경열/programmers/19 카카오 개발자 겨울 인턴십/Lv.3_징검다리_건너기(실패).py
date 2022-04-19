def solution(stones, k):
    answer = 0
    i = 0
    cnt = 0

    while True:
        if cnt == k:
            break

        if i == len(stones):
            answer += 1
            i, cnt = 0, 0

        if stones[i]:
            stones[i] -= 1
            cnt = 0
        else:
            cnt += 1

        i += 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))