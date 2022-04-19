def solution(s):
    answer = []
    tmp = list(s[1:-2].split('}'))
    lst = []
    for t in tmp:
        t = t[1:]
        t = t.replace('{', '')
        lst.append(list(t.split(',')))
    lst.sort(key=len)
    for nums in lst:
        for num in nums:
            if int(num) not in answer:
                answer.append(int(num))
                break
    return answer


str1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
str2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(str1))