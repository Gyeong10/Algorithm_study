test = int(input())

for t in range(1,test+1):
    hour_1, minute_1, hour_2, minute_2 = map(int,input().split())
    hour = hour_1 + hour_2
    minute = minute_1 + minute_2
    
    #분이 60이상일 때 0~59 사이로 바꾸기
    if minute >= 60:
        minute = minute % 60
        hour += 1
    
    #시가 12보다 클때 1~12 사이로 바꾸기
    if hour > 12:
        if hour == 24:
            hour = 12
        else:
            hour = hour % 12
    
    print(f'#{t} {hour} {minute}')

