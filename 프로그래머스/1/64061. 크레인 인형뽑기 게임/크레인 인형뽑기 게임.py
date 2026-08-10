def solution(board, moves):
    answer = 0
    bowl = []

    for y in moves:
        y -= 1
        for x in range(len(board)):
            if board[x][y] != 0:
                if len(bowl) > 0 and bowl[-1] == board[x][y]:
                    bowl.pop()
                    answer += 2

                else:
                    bowl.append(board[x][y])

                board[x][y] = 0
                break

    return answer