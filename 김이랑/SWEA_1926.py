num = int(input())

for i in range(1, num + 1):
    str_num = str(i)
    bar = 0
    if '3' in str_num or '6' in str_num or '9' in str_num:
        bar = str_num.count('3')
        bar = str_num.count('6') + bar
        bar = str_num.count('9') + bar
        print('-'*bar, end = ' ')
        continue
    print(str_num, end=' ')
