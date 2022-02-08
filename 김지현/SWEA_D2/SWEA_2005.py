tests = int(input())

for t in range(1,tests+1):
    n = int(input())

    #pascla[0][0] = 1로 지정
    pascal = [[1]]
    for i in range(1,n):
        part_pascal = []
        for j in range(i+1):
            
            #pascal[i][0], pascal[i][1]일 때 1
            if j == 0 or j == i:
                part_pascal.append(1)
            
            #아니면 덧셈 진행
            else:
                part_pascal.append(pascal[i-1][j-1]+pascal[i-1][j])
        
        #pascal list안에 part_pascal list추가해줘서 2차원 배열로 만듦
        pascal.append(part_pascal)
    
    #출력
    print(f'#{t}')
    for i in range(len(pascal)):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()