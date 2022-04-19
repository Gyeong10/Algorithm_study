from itertools import permutations

def check(users, banned_id):
    for k in range(len(users)):
        # 길이가 다르면 같을 수 없기 때문에 False 반환
        if len(users[k]) != len(banned_id[k]):
            return False
        # 별표처리부분이면 넘기고 만약 알파벳이 다르다면 False 반환
        for t in range(len(users[k])):
            if banned_id[k][t] == '*':
                continue
            if banned_id[k][t] != users[k][t]:
                return False
    # 다 같으면 True 반환
    return True


def solution(user_id, banned_id):
    answer = 0
    # 각 user로 나올 수 있는 조합 다 구하기
    user_perm = list(permutations(user_id, len(banned_id)))
    ban_lst = []
    # 나온 조합과 banned_id를 확인해 가능하면 ban_lst에 있는지 확인하고 추가
    for users in user_perm:
        if not check(users, banned_id):
            continue
        else:
            # set으로 바꿔서 순서가 바뀌어도 같은 것으로 처리하게 함
            users = set(users)
            if users not in ban_lst:
                ban_lst.append(users)
    answer = len(ban_lst)
    return answer


u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b1 = ["fr*d*", "abc1**"]
b2 = ["*rodo", "*rodo", "******"]
b3 = ["fr*d*", "*rodo", "******", "******"]
print(solution(u, b3))