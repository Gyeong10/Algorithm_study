N = int(input())
max_cnt = 0
for i in range(1,N+1):
    cnt = 2
    tmp = [N, i]
    while tmp[cnt-2] - tmp[cnt-1] >= 0:
        tmp.append(tmp[cnt-2] - tmp[cnt-1])
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        result = tmp
print(max_cnt)
for i in result:
    print(i, end = ' ')