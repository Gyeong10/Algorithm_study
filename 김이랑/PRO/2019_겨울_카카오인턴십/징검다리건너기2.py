def check(stones, k, mid):
    jump_check = k
    for stone in stones:
        if stone - mid <= 0:
            jump_check -= 1
            if jump_check == 0:
                return False
        else:
            jump_check = k
    return True


def solution(stones, k):
    answer = 0
    max_ni = max(stones)
    min_ni = 1
    while min_ni <= max_ni:
        check_ni = (max_ni+min_ni) // 2
        if check(stones, k, check_ni):
            answer = check_ni
            min_ni = check_ni + 1
        else:
            max_ni = check_ni - 1
    return answer + 1


arr1 = [1, 1, 1, 1, 1]
n = 3
print(solution(arr1, n))