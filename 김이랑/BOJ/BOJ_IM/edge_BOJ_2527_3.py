for _ in range(4):
    answer = ''
    x_1, y_1, p_1, q_1, x_2, y_2, p_2, q_2 = map(int, input().split())
    if (x_1 == p_2 and y_1 == q_2) or (p_1 == x_2 and q_1 == y_2) or (x_1 == p_2 and q_1 == y_2) or (p_1 == x_2 and q_1 == y_2):
        answer = 'c'
    elif q_1 < y_2 or p_1 < x_2 or p_2 < x_1 or q_1 < y_2:
        answer = 'd'
    elif (x_1<=x_2 and y_2<=y_1) or (x_1>x_2 and y_1<y_2):
        answer = 'a'
    elif x_1<=x_2<p_1:
        if (y_1<=y_2<q_1) or (y_1<q_2<=q_1):
            answer = 'a'
    elif x_1<=p_2<p_1:
        if ((q_1<y_2<=y_1) or (y_1<=q_2<q_1)):
            answer = 'a'
    else:
        answer = 'b'

    print(answer)