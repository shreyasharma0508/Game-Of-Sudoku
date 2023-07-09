def is_valid(board, row, col, num):
    # Check the row
    for x in range(9):
        if board[row][x] == num:
            return False
             
    # Check the column
    for x in range(9):
        if board[x][col] == num:
            return False
 
    # Check the box
    start_row, start_col = row - row%3, col - col%3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num

                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# driver code
if __name__ == "__main__":
 
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    if (solve_sudoku(board)):
        for i in board:
            print(i)
    else:
        print("No solution exists.")