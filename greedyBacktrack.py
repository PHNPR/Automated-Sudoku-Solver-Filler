from utilities import isSafe, printBoard, assign

def greedyBacktrack(board):
    min = 9
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                count = 0
                for val in range(1,10):
                    if(isSafe(board, i, j, val)):
                        count = count + 1 
                if(count < min): 
                    min = count
                    row = i
                    col = j
    if(min == 9):
        return True 
    for val in range(1,10):
        if(isSafe(board, row, col, val)):
            board[row][col] = val 
            if(greedyBacktrack(board)):
                return True 
            board[row][col] = 0 
    return False 

def greedyBacktrack_visualiser(board, curr_row = 0, curr_col = 0):
    min = 9
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                count = 0
                for val in range(1,10):
                    if(isSafe(board, i, j, val)):
                        count = count + 1
                if(count < min): 
                    min = count
                    row = i
                    col = j
    if(min == 9):
        return True, curr_row, curr_col 
    for val in range(1,10):
        if(isSafe(board, row, col, val)):
            curr_row, curr_col = assign(board, row, col, val, curr_row, curr_col) 
            return_value, curr_row, curr_col = greedyBacktrack_visualiser(board ,curr_row, curr_col)
            if(return_value):
                return True, curr_row, curr_col 
            curr_row, curr_col = assign(board, row, col, 0, curr_row, curr_col) 
    return False, curr_row, curr_col 

if '__main__' == __name__:
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 0, 7, 8, 9, 1, 0, 3],
            [7, 8, 9, 1, 2, 3, 4, 0, 6],
            [2, 3, 0, 0, 6, 7, 8, 0, 1],
            [5, 6, 7, 8, 9, 1, 2, 0, 4],
            [8, 9, 0, 2, 3, 4, 5, 0, 7],
            [3, 0, 5, 6, 7, 8, 0, 1, 2],
            [6, 7, 0, 9, 1, 2, 3, 0, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
            
    if(greedyBacktrack(board)):
        print("Sudoku solved")
        printBoard(board)  
    else:
        print("No solution")