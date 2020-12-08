#Brittany Sundberg
#CS 325 HW 8
#Fall 2020 12/7/20




GameBoard = [[6, " ", " ", " ", 1, " ", " ", 8, " "],
             [" ", " ", " ", " ", 5, " ", " ", 3, " "],
             [2, " ", " ", 8, " ", " ", 5, " ", " "],
             [" ", " ", " ", " ", 3, 5, " ", 7, " "],
             [8, " ", " ", 9, " ", " ", " ", " ", 2],
             [" ", " ", 3, " ", " ", 8, 6, " ", " "],
             [3, " ", 2, " ", " ", 9, " ", " ", 4],
             [" ", " ", " ", " ", " ", 1, 8, " ", " "],
             [" ", " ", 8, 7, 6, " ", " ", " ", " "]]


ColHeaders = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]


def PrintBoard():
    print("         ", ColHeaders[0], " ", ColHeaders[1], " ", ColHeaders[2], "  ", ColHeaders[3], " ", ColHeaders[4], " ", ColHeaders[5], "  ", ColHeaders[6], " ", ColHeaders[7], " ", ColHeaders[8])
    print("        -------------------------------------------------")
    print("Row 1   | ", GameBoard[0][0], "  ", GameBoard[0][1], "  ", GameBoard[0][2], " | ", GameBoard[0][3], "  ", GameBoard[0][4], "  ", GameBoard[0][5], " | ", GameBoard[0][6], "  ", GameBoard[0][7], "  ", GameBoard[0][8], " | ")
    print("Row 2   | ", GameBoard[1][0], "  ", GameBoard[1][1], "  ", GameBoard[1][2], " | ", GameBoard[1][3], "  ", GameBoard[1][4], "  ", GameBoard[1][5], " | ", GameBoard[1][6], "  ", GameBoard[1][7], "  ", GameBoard[1][8], " | ")
    print("Row 3   | ", GameBoard[2][0], "  ", GameBoard[2][1], "  ", GameBoard[2][2], " | ", GameBoard[2][3], "  ", GameBoard[2][4], "  ", GameBoard[2][5], " | ", GameBoard[2][6], "  ", GameBoard[2][7], "  ", GameBoard[2][8], " | ")
    print("        -------------------------------------------------")
    print("Row 4   | ", GameBoard[3][0], "  ", GameBoard[3][1], "  ", GameBoard[3][2], " | ", GameBoard[3][3], "  ", GameBoard[3][4], "  ", GameBoard[3][5], " | ", GameBoard[3][6], "  ", GameBoard[3][7], "  ", GameBoard[3][8], " | ")
    print("Row 5   | ", GameBoard[4][0], "  ", GameBoard[4][1], "  ", GameBoard[4][2], " | ", GameBoard[4][3], "  ", GameBoard[4][4], "  ", GameBoard[4][5], " | ", GameBoard[4][6], "  ", GameBoard[4][7], "  ", GameBoard[4][8], " | ")
    print("Row 6   | ", GameBoard[5][0], "  ", GameBoard[5][1], "  ", GameBoard[5][2], " | ", GameBoard[5][3], "  ", GameBoard[5][4], "  ", GameBoard[5][5], " | ", GameBoard[5][6], "  ", GameBoard[5][7], "  ", GameBoard[5][8], " | ")
    print("        -------------------------------------------------")
    print("Row 7   | ", GameBoard[6][0], "  ", GameBoard[6][1], "  ", GameBoard[6][2], " | ", GameBoard[6][3], "  ", GameBoard[6][4], "  ", GameBoard[6][5], " | ", GameBoard[6][6], "  ", GameBoard[6][7], "  ", GameBoard[6][8], " | ")
    print("Row 8   | ", GameBoard[7][0], "  ", GameBoard[7][1], "  ", GameBoard[7][2], " | ", GameBoard[7][3], "  ", GameBoard[7][4], "  ", GameBoard[7][5], " | ", GameBoard[7][6], "  ", GameBoard[7][7], "  ", GameBoard[7][8], " | ")
    print("Row 9   | ", GameBoard[8][0], "  ", GameBoard[8][1], "  ", GameBoard[8][2], " | ", GameBoard[8][3], "  ", GameBoard[8][4], "  ", GameBoard[8][5], " | ", GameBoard[8][6], "  ", GameBoard[8][7], "  ", GameBoard[8][8], " | ")
    print("        -------------------------------------------------")
    return


def MakeMove(row, column, value):
    """makes a move on the board by setting the value to the user's input."""
    if (row == 1 and column == 1) or (row == 1 and column == 5) or (row == 1 and column == 8) or (row == 2 and column == 5) or \
            (row == 2 and column == 8) or (row == 3 and column == 1) or (row == 3 and column == 4) or (row == 3 and column == 7) or \
            (row == 4 and column == 5) or (row == 4 and column == 6) or (row == 4 and column == 8) or (row == 5 and column == 1) or \
            (row == 5 and column == 4) or (row == 5 and column == 9) or (row == 6 and column == 3) or (row == 6 and column == 6) or \
            (row == 6 and column == 7) or (row == 7 and column == 1) or (row == 7 and column == 3) or (row == 7 and column == 6) or \
            (row == 7 and column == 9) or (row == 8 and column == 6) or (row == 8 and column == 7) or (row == 9 and column == 3) or \
            (row == 9 and column == 4) or (row == 9 and column == 5) :
        print("Sorry, that's a pre-set number that can't be changed. Try another move.")
        return
    if type(value) != int:
        print("Sorry, you can only put numbers on the board. Try again with a number")
        return
    if row > 9 or row < 1 or column > 9 or column < 1:
        print("Sorry, you've entered a row or column that does not exist. Try again but check your row and column numbers")
        return
    GameBoard[row-1][column-1] = value
    print("move successfully made! Here's an updated version of your board:")
    PrintBoard()
    return


def CheckMyAnswer():
    """checks to see if the user's answer (completed board) is correct.
    First checks to make sure the board is full
    Next checks all the rows
    Next checks all the columns
    Next checks each 3x3 square
    If all that checks out, then it means the answer works!"""

    #check if the board is full
    for array in GameBoard:
        if " " in array:
            print("Looks like you still have an empty space! Fill the board before checking your answer.")
            return


    #check all the rows to make sure they all have 1-9 in them:
    rowNum = 1
    for array in GameBoard:
        if (1 in array) and (2 in array) and (3 in array) and (4 in array) and (5 in array) and (6 in array) and (7 in array) and (8 in array) and (9 in array):
            print("Row ", rowNum, " looks good!")
            rowNum += 1
        else:
            print("Uh oh! Looks like there's a problem with Row ", rowNum)
            return

    #check all the columns to make sure they all have 1-9 in them
    colNum = 1
    while colNum < 10:
        newArray = []
        for array in GameBoard:
            newArray.append(array[colNum-1])
        if (1 in newArray) and (2 in newArray) and (3 in newArray) and (4 in newArray) and (5 in newArray) and (6 in newArray) and (7 in newArray) and (8 in newArray) and (9 in newArray):
            print("Column ", colNum, " looks good!")
            colNum += 1
        else:
            print("Uh oh! Looks like there's a problem with Column ", colNum)
            return



    #check all the squares to see if they all have 1-9 in them
    #top left square is row indexes 0-2 and col indexes 0-2
    colIndex = 0
    topLeft = []
    while colIndex < 3:
        for i in range(0, 3):
            topLeft.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in topLeft) and (2 in topLeft) and (3 in topLeft) and (4 in topLeft) and (5 in topLeft) and (6 in topLeft) and (7 in topLeft) and (8 in topLeft) and (9 in topLeft):
        print("Top Left Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Top Left Square.")
        return


    #top middle square is row indexes 0-2 and col indexes 3-5
    colIndex = 3
    topMid = []
    while colIndex < 6:
        for i in range(0, 3):
            topMid.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in topMid) and (2 in topMid) and (3 in topMid) and (4 in topMid) and (5 in topMid) and (6 in topMid) and (7 in topMid) and (8 in topMid) and (9 in topMid):
        print("Top Middle Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Top Middle Square.")
        return




    #top right square is row indexes 0-2 and col indexes 6-8
    colIndex = 6
    topRight = []
    while colIndex < 9:
        for i in range(0, 3):
            topRight.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in topRight) and (2 in topRight) and (3 in topRight) and (4 in topRight) and (5 in topRight) and (6 in topRight) and (7 in topRight) and (8 in topRight) and (9 in topRight):
        print("Top Right Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Top Right Square.")
        return




    #mid left square is row indexes 3-5 and col indexes 0-2
    colIndex = 0
    midLeft = []
    while colIndex < 3:
        for i in range(3, 6):
            midLeft.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in midLeft) and (2 in midLeft) and (3 in midLeft) and (4 in midLeft) and (5 in midLeft) and (6 in midLeft) and (7 in midLeft) and (8 in midLeft) and (9 in midLeft):
        print("Middle Left Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Middle Left Square.")
        return


    #mid middle square is row indexes 3-5 and col indexes 3-5
    colIndex = 3
    midMid = []
    while colIndex < 6:
        for i in range(3, 6):
            midMid.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in midMid) and (2 in midMid) and (3 in midMid) and (4 in midMid) and (5 in midMid) and (6 in midMid) and (7 in midMid) and (8 in midMid) and (9 in midMid):
        print("Center Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Center Square.")
        return



    #mid right square is row indexes 3-5 and col indexes 6-8
    colIndex = 6
    midRight = []
    while colIndex < 9:
        for i in range(3, 6):
            midRight.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in midRight) and (2 in midRight) and (3 in midRight) and (4 in midRight) and (5 in midRight) and (6 in midRight) and (7 in midRight) and (8 in midRight) and (9 in midRight):
        print("Middle Right Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Middle Right Square.")
        return




    #bottom left square is row indexes 6-8 and col indexes 0-2
    colIndex = 0
    bottomLeft = []
    while colIndex < 3:
        for i in range(6, 9):
            bottomLeft.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in bottomLeft) and (2 in bottomLeft) and (3 in bottomLeft) and (4 in bottomLeft) and (5 in bottomLeft) and (6 in bottomLeft) and (7 in bottomLeft) and (8 in bottomLeft) and (9 in bottomLeft):
        print("Bottom Left Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Bottom Left Square.")
        return


    #bottom middle square is row indexes 6-8 and col indexes 3-5
    colIndex = 3
    bottomMid = []
    while colIndex < 6:
        for i in range(6, 9):
            bottomMid.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in bottomMid) and (2 in bottomMid) and (3 in bottomMid) and (4 in bottomMid) and (5 in bottomMid) and (6 in bottomMid) and (7 in bottomMid) and (8 in bottomMid) and (9 in bottomMid):
        print("Bottom Middle Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Bottom Middle Square.")
        return


    #bottom right square is row indexes 6-8 and col indexes 6-8
    colIndex = 6
    bottomRight = []
    while colIndex < 9:
        for i in range(6, 9):
            bottomRight.append(GameBoard[i][colIndex])
        colIndex += 1
    if (1 in bottomRight) and (2 in bottomRight) and (3 in bottomRight) and (4 in bottomRight) and (5 in bottomRight) and (6 in bottomRight) and (7 in bottomRight) and (8 in bottomRight) and (9 in bottomRight):
        print("Bottom Right Square looks good!")
    else:
        print("Uh oh! Looks like there's a problem with the Bottom Right Square.")
        return

    print("Everything checks out! Your answer is correct!")
    return


print("Welcome to Sudoku!")
print("Sudoku is a game where you need to enter numbers 1 through 9 in each square of the board.")
print("To win the game, each row, column, and 3x3 square on the board (indicated with lines) needs to have each number 1-9 in it with no duplicates.")
print("To print the game board at any time, type 'PrintBoard()' and hit enter.")
print("To make a move (enter a number on the board) type 'MakeMove()' and put the Row Number, Column Number, and value you're entering into the parenthesis, then hit enter.")
print("For example, to put a 4 in the Row 3 Column 9 spot, type 'MakeMove(3, 9, 4)' and hit enter.")
print("When your board is full and you are ready to check to see if your solution is correct, type 'CheckMyAnswer()' and hit enter.")
print("Enjoy the game! Here is your board:")
PrintBoard()

#for testing only:
"""
MakeMove(1, 1, 6)
MakeMove(1, 2, 5)
MakeMove(1, 3, 9)
MakeMove(1, 4, 3)
MakeMove(1, 5, 1)
MakeMove(1, 6, 4)
MakeMove(1, 7, 2)
MakeMove(1, 8, 8)
MakeMove(1, 9, 7)


MakeMove(2, 1, 1)
MakeMove(2, 2, 8)
MakeMove(2, 3, 7)
MakeMove(2, 4, 6)
MakeMove(2, 5, 5)
MakeMove(2, 6, 2)
MakeMove(2, 7, 4)
MakeMove(2, 8, 3)
MakeMove(2, 9, 9)


MakeMove(3, 1, 2)
MakeMove(3, 2, 3)
MakeMove(3, 3, 4)
MakeMove(3, 4, 8)
MakeMove(3, 5, 9)
MakeMove(3, 6, 7)
MakeMove(3, 7, 5)
MakeMove(3, 8, 1)
MakeMove(3, 9, 6)

MakeMove(4, 1, 4)
MakeMove(4, 2, 2)
MakeMove(4, 3, 6)
MakeMove(4, 4, 1)
MakeMove(4, 5, 3)
MakeMove(4, 6, 5)
MakeMove(4, 7, 9)
MakeMove(4, 8, 7)
MakeMove(4, 9, 8)


MakeMove(5, 1, 8)
MakeMove(5, 2, 7)
MakeMove(5, 3, 1)
MakeMove(5, 4, 9)
MakeMove(5, 5, 4)
MakeMove(5, 6, 6)
MakeMove(5, 7, 3)
MakeMove(5, 8, 5)
MakeMove(5, 9, 2)


MakeMove(6, 1, 5)
MakeMove(6, 2, 9)
MakeMove(6, 3, 3)
MakeMove(6, 4, 2)
MakeMove(6, 5, 7)
MakeMove(6, 6, 8)
MakeMove(6, 7, 6)
MakeMove(6, 8, 4)
MakeMove(6, 9, 1)


MakeMove(7, 1, 3)
MakeMove(7, 2, 1)
MakeMove(7, 3, 2)
MakeMove(7, 4, 5)
MakeMove(7, 5, 8)
MakeMove(7, 6, 9)
MakeMove(7, 7, 7)
MakeMove(7, 8, 6)
MakeMove(7, 9, 4)


MakeMove(8, 1, 7)
MakeMove(8, 2, 6)
MakeMove(8, 3, 5)
MakeMove(8, 4, 4)
MakeMove(8, 5, 2)
MakeMove(8, 6, 1)
MakeMove(8, 7, 8)
MakeMove(8, 8, 9)
MakeMove(8, 9, 3)


MakeMove(9, 1, 9)
MakeMove(9, 2, 4)
MakeMove(9, 3, 8)
MakeMove(9, 4, 7)
MakeMove(9, 5, 6)
MakeMove(9, 6, 3)
MakeMove(9, 7, 1)
MakeMove(9, 8, 2)
MakeMove(9, 9, 5)

CheckMyAnswer()
"""