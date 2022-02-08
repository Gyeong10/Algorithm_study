import sys
sys.stdin = open('input.txt', 'r')

test = int(input())

for t in range(1,test+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        row = []
        column = []
        for j in range(9):
            #행 확인
            if puzzle[i][j] not in row:
                row.append(puzzle[i][j])
            else:
                result = 0
                break
            #열 확인
            if puzzle[j][i] not in column:
                column.append(puzzle[j][i])
            else:
                result = 0
                break
            #격자 확인
            grid = []
            if i % 3 == 0 and j % 3 == 0:
                for k in range(3):
                    for l in range(3):
                        if puzzle[i+k][j+l] not in grid:
                            grid.append(puzzle[i+k][j+l])
                        else:
                            result = 0
                            break
    print(f'#{t} {result}')


#시간 줄일 방법 찾기 (set 이용해보기)
