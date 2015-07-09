
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
    if check_move_valid(board, row, col, row2, col2):
      board[row2][col2] = board[row][col]
      board[row][col] = ' '

def check_move_valid(board, initial_row, initial_col, final_row, final_col):
    valid_horizontal = (final_col - initial_col == 1 or final_col - initial_col == -1)

    if final_col > 7 or final_row > 7 or final_row <0 or final_col <0:
      print final_row, final_col, "NO >7"
      return False
    elif board[initial_row][initial_col] == 'x':
      if final_row - initial_row == 1 and valid_horizontal:
        return True
      else:
        print "NO x can't move there"
        return False
    elif board[initial_row][initial_col] == 'o':
      if final_row - initial_row == 1 and valid_horizontal:
        return True
      else:
        print "NO o can't move there"
        return False
    else:
      print "nothing happened"





board = initial_board()
move(board, 2, 0, 3, 1)
move(board, 3, 1, 4, 0)

display(board)
