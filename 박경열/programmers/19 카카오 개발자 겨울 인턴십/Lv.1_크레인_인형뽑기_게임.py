def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for num in moves:
        for i in range(N):
            if board[i][num - 1]:
                stack.append([board[i][num - 1]])
                board[i][num - 1] = 0
                break

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))