def solution(board, moves):
    answer = 0
    stack = []
    for now in moves:
        col = now - 1
        for i in range(len(board[0])):
            if board[i][col]:
                new = board[i][col]
                board[i][col] = 0
                if stack and (stack[-1] == new):
                    stack.pop()
                    answer += 2
                    break
                stack.append(new)
                break
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))