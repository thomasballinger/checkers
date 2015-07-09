
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

def prompt_user():
  print ("Which piece you want to move!?")
  old_user_column = int(raw_input("Row: "))
  old_user_row = int(raw_input("Column: "))

  print("Where you wanna move it!?")
  new_spot_row = int(raw_input("Row: "))
  new_spot_col = int(raw_input("Column: "))
  
  return [old_user_row, old_user_column, new_spot_row, new_spot_col]
  #some sort of checking in here?


board = initial_board()

display(board)
print(prompt_user())
