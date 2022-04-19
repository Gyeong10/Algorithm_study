def solution(s):
    answer = []
    s = s[1:-1]
    list_s = []

    temp = ''
    for now_s in s:
        if now_s == '{':
            temp = ''
        elif now_s == '}':
            list_s.append(temp.split(','))
        else:
            temp+=now_s

    sort_s = [[] for _ in range(len(list_s))]
    now_len = 1
    for now_s in list_s:
        sort_s[len(now_s)-1] = now_s
        now_len += 1

    for now_s in sort_s:
        for now_num in now_s:
            if int(now_num) not in answer:
                answer.append(int(now_num))

    return answer

print(solution("{{20,111},{111}}"))