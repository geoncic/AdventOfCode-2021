def dayFour():
    numbers, all_boards = readFile()
    solved_boards = solve_board(all_boards, numbers)
    print(f'Part One First Board Score is: {returnScore(solved_boards, "first")}')
    print(f'Part Two Last Board Score is: {returnScore(solved_boards, "last")}')


def solve_board(all_boards, numbers):
    board_map = create_map(all_boards)
    solved_boards = []
    for n, number in enumerate(numbers):
        for b, board in enumerate(board_map):
            for row, i in enumerate(board[:-1]):
                for col, j in enumerate(i[:-1]):
                    if number == j:
                        board_map[b][row][5] -= 1
                        board_map[b][5][col] -= 1
                        board_map[b][row][col] = 'x'
                        solved = check_solved(board)
                        if solved:
                            board_map[b][5][5] = (b, number, n)
                            solved_boards.append(board_map[b])
                            board_map[b] = []
    return solved_boards


def returnScore(boards, position):
    if position == 'first':
        return score_board(boards[0])
    elif position == 'last':
        return score_board(boards[-1])
    else:
        return 'Need to select either "first" or "last"...'


def score_board(board):
    score = 0
    for i in board[:-1]:
        if isinstance(i, int):
            score += i
        for j in i[:-1]:
            if isinstance(j, int):
                score += j
    score = score*board[5][5][1]
    return score


def check_solved(board):
    for row, i in enumerate(board[:-1]):
        for col, j in enumerate(i[5:]):
            if j == -5:
                return True
    for x, n in enumerate(board[-1][:-1]):
        if n == -5:
            return True


def create_map(all_boards):
    for board in all_boards:
        board.append([0]*(len(board)))
        for row in board:
            row.append(0)
    return all_boards


def readFile():
    with open('input.txt') as f:
        numbers, *boards = f.read().split('\n\n')
        numbers = [int(i) for i in numbers.split(',')]
        all_boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]
        return numbers, all_boards


if __name__ == "__main__":
    dayFour()
