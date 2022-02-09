test_num = int(input())

for i in range(1, test_num + 1):
    num = int(input())
    print(f'#{i}')
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1
#     1 5 10 10 5 1
#     1 6 15 20 15 6 1

    # 0개일 때 예외처리 하긴 해야할듯?
    triangle = [[1]]
    for j in range(1, num):
        triangle.append([])
        for k in range(j+1): # 1, 0
            if k-1 < 0 :
                triangle[j].append(0 + triangle[j-1][k])
            elif j == k:
                triangle[j].append(triangle[j-1][k-1] + 0)
            else:
                triangle[j].append(triangle[j-1][k-1] + triangle[j-1][k])

    for row in range(len(triangle)):
        for col in range(len(triangle[row])):
            print(triangle[row][col], end = ' ')
        print()