
def display(board):
    for row in board:
        print row

def initial_board():
    top = [['x' if col % 2 == row % 2 else ' '
            for col in range(8)]
          for row in range(3)]

    middle = [[' '] * 8 for x in range(2)]

    bottom = [['o' if col % 2 != row % 2 else ' '
               for col in range(8)]
              for row in range(3)]
    board = top + middle + bottom
    return board

def move(board, row, col, row2, col2):
    board[row2][col2] = board[row][col]
    board[row][col] = ' '

board = initial_board()

display(board)
