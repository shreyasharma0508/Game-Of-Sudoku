# Game Of Sudoku
This repository contains a simple Sudoku game implemented in Python. It includes both a terminal-based version and a GUI version. The game solves a Sudoku puzzle using a backtracking algorithm.

## File Descriptions
### sudoku_solver.py
#### is_valid(board, row, col, num) function
This function checks whether a number can be placed at a given position in the Sudoku grid.

The function checks the specific row, column, and 3x3 box for the presence of the number. If the number is not present, it returns True; otherwise, False.

The 3x3 box check calculates the starting indices of the box and then iterates through it for a match. The formulae start_row = row - row%3 and start_col = col - col%3 are used to get the top-left cell of the 3x3 box containing the given cell.

The time complexity is O(n), as it checks for the number's presence in the respective row, column, and 3x3 box. Each check takes O(n) time.

#### solve_sudoku(board) function
This function solves the Sudoku puzzle using the backtracking algorithm.

It iterates through each cell of the grid, and when it finds an empty cell (marked with 0), it tries to fit a number from 1 to 9.

If a number fits, it recursively tries to fill the next empty cell. If no number can be placed in a certain cell, it backtracks to the previous cells and tries different numbers.

The base case for the recursion is when the grid is completely filled. At this point, the function returns True.

The time complexity is O(n^4), due to the recursion and iterative processes. For each empty cell, it iterates over n possible numbers. For each number, it makes a recursive call to solve_sudoku(board). In the worst-case scenario, the function has to iterate through each cell in the grid (n^2 cells for an n x n grid) and for each cell, iterate through n possibilities.

#### Driver Code
The driver code defines the Sudoku grid and calls the solve_sudoku(board) function.

The 9x9 Sudoku grid is represented as a 2D list, with empty cells denoted by 0.

The solve_sudoku(board) function is called to solve the puzzle. If a solution is found, the solved grid is printed. Otherwise, it prints "No solution exists".

### sudoku_gui.py
This file contains the code for the GUI version of the game.

The draw_numbers() function draws the numbers on the Sudoku grid. It uses the blit() function to draw on the screen.

The main game loop handles event checking (such as clicking the close button), clearing the screen, drawing the grid and the numbers, and updating the screen.

If you uncomment the time.sleep(3); solve_sudoku(board) line, it will solve the Sudoku automatically after 3 seconds.

## Usage
To solve a Sudoku puzzle, define your puzzle in the driver code section as a 2D list (with 0s representing empty cells) and run the script. The solution will be printed in the console. For the GUI version, run the sudoku_gui.py file.

## Requirements
Python 3.x
Pygame for the GUI version
Note: This project is meant to be a demonstration of a backtracking algorithm to solve Sudoku puzzles, and as such, does not include functionality for inputting custom puzzles in the GUI version.
