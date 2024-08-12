import pyautogui as pg
pg.PAUSE = 0

def isSafe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if(j == 2 or j == 5):
                print("|", end=" ")
        if(i == 2 or i == 5):
            print("\n- - - - - - - - - - -")
        else:
            print("\n")

def getInput():
    board = []
    for i in range(9): 
        board.append(list(map(int, input().split()))) 
    return board

def assign(board, row, col, num, curr_row = 0, curr_col = 0):
    board[row][col] = num
    if(row<curr_row):
        pg.press('up', presses=curr_row-row)
    elif(row>curr_row):
        pg.press('down', presses=row-curr_row)
    if(col<curr_col):
        pg.press('left', presses=curr_col-col)
    elif(col>curr_col):
        pg.press('right', presses=col-curr_col)
    if(num == 0):
        pg.press('backspace')
    else:
        pg.press(str(num))
    curr_row = row
    curr_col = col
    return curr_row, curr_col

def EnterBoard(board): 
    for i in range(9):
        for j in range(9):
            pg.press(board[i][j])
            if(j != 8):
                pg.press('right')
            if(j == 8 and i != 8):
                pg.press('down')
                pg.press('left', presses = 8)
            if(j == 8 and i == 8):
                pg.press('enter')

def ConvertToChar(board): 
    grid_char = []
    for i in range(9):
        grid_char.append([])
        for j in range(9):
            grid_char[i].append(str(board[i][j]))
    return grid_char