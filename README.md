# Game-Of-Sudoku

1. The is_valid(board, row, col, num) function

a)This function checks if a number can be placed at a given position. 

b)It does so by checking the row, column and 3x3 box for the presence of that number. 

c)If the number is not present, it returns True else False (Iteration)

d)The box check calculates the start indices of the box and then iterates through it for a match. 

e)The formulae start_row = row - row%3 and start_col = col - col%3 get the top-left cell of the 3x3 box in which the given cell falls.

f)Big O: O(n) because it checks the number's presence in the respective row, column, and 3x3 box, each taking O(n) time (where n is the size of the Sudoku board, in this case n=9). Therefore, the time complexity is O(n + n + n) = O(n). 

2. The solve_sudoku(board) function
   
-This function solves the sudoku puzzle using backtracking.
-It iterates through each cell of the board, and when it finds an empty cell (with 0), it tries to fit in a number from 1 to 9.
-If the number fits, it recursively tries to fill the next empty cell. 
-If a cell is found where no number fits, it backtracks, changing the previous cells, and tries to fit in another number.
-The function iterates through the entire board using nested loops for rows and columns. 
-If an empty cell (with 0) is found, it then iterates from 1 to 9 to try and find a number that can fit there.
-If a number is valid (i.e., is_valid(board, row, col, num) returns True), it places that number there and makes a recursive call to solve_sudoku(board).
-If the recursive call returns True, it means the remaining board could be filled successfully, and the function returns True.
-If the function has tried all numbers from 1 to 9 and none could be placed in a certain cell, it resets that cell (backtracks) and returns False.
-The base case for the recursion is when the board is completely filled, which happens when the function has iterated over all cells and hasn't found any empty cells. In this case, the function returns True.
-Big O: O(n^4) because this function is a bit more complex because it involves recursion. For each empty cell, it tries every possible number, and for each number, it makes a recursive call. There are n^2 cells in the Sudoku board (n being 9 for a 9x9 Sudoku). In the worst-case scenario (an empty board), each cell could potentially go through n iterations. For each of these, the is_valid function is called which again takes O(n) time. Thereby, the time complexity is O((n^2)nn) = O(n^4). This obviously would be the worst-case time complexity, corresponding to a completely empty Sudoku board.

3. The Driver code
   
-This is where the sudoku board is defined and the solve_sudoku(board) function is called.
-The 9x9 sudoku board is represented as a 2D list. Empty cells are denoted by 0.
-The solve_sudoku(board) function is called to solve the puzzle. 
-If a solution is found, the solved board is printed. Otherwise, it prints "No solution exists".
