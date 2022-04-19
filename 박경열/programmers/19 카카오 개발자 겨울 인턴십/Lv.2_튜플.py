def solution(s):
    answer = []
    visited = [0] * 100001
    used = [0] * 100001
    stack = []
    numbers = []

    sstr = ''
    for t in range(1, len(s) - 1):

        if s[t] == '{':
            stack.append(s[t])

        elif s[t] == ',' and stack:
            numbers.append(int(sstr))
            sstr = ''

        elif s[t] == ',' and not stack:
            pass

        elif s[t] == '}':
            stack.pop()
            numbers.append(int(sstr))
            sstr = ''
            visited[len(numbers)] = numbers
            numbers = []
        # 숫자
        else:
            sstr += s[t]


    for i in range(1, len(visited)):
        if not visited[i]:
            break

        for num in visited[i]:
            if not used[num]:
                answer.append(num)
                used[num] = 1
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))