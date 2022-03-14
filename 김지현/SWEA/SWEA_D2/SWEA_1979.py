import sys
sys.stdin = open('input.txt','r')
tests = int(input())

for t in range(1,tests+1):
    n, k = map(int, input().split())
    #퍼즐 흰색/검은색 2차원 배열로 입력 받기
    puzzle = [list(map(int,input().split())) for _ in range(n)]

    able = []

    for i in range(n):
        row = 0
        column = 0
        for j in range(n):
            #가로
            if puzzle[i][j] == 1:
                row += 1
            else:
                able.append(row)
                row = 0
            
            #세로
            if puzzle [j][i] == 1:
                column += 1
            else:
                able.append(column)
                column = 0
            
            #마지막 행/열일때 추가
            if j == n-1:
                able.append(row)
                able.append(column)

    print(f'#{t} {able.count(k)}')