from itertools import permutations


def solution(user_id, banned_id):
    answer_list = []
    user_lists = permutations(user_id, len(user_id))

    for user_list in user_lists:
        temp = []
        for banned in banned_id:
            for user in user_list:
                if user in temp:
                    continue
                elif len(banned) == len(user):
                    flag = 1
                    for i in range(len(user)):
                        if banned[i] == '*' or banned[i] == user[i]:
                            continue
                        else:
                            flag = 0
                            break
                    if flag:
                        temp.append(user)
                        break
        temp.sort()
        if len(temp) == len(banned_id) and temp not in answer_list:
            answer_list.append(temp)
    return len(answer_list)


arr1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
arr2 = ["*rodo", "*rodo", "******"]
print(solution(arr1, arr2))