sudoku = [
        [3, 0, 6,  5, 0, 8,  4, 0, 0],
        [5, 2, 0,  0, 0, 0,  0, 0, 0],
        [0, 8, 7,  0, 0, 0,  0, 3, 1],

        [0, 0, 3,  0, 1, 0,  0, 8, 0],
        [9, 0, 0,  8, 6, 3,  0, 0, 5],
        [0, 5, 0,  0, 9, 0,  6, 0, 0],

        [1, 3, 0,  0, 0, 0,  2, 5, 0],
        [0, 0, 0,  0, 0, 0,  0, 7, 4],
        [0, 0, 5,  2, 0, 6,  3, 0, 0]
]


def display(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
            if j == 2 or j == 5:
                print('|', end=' ')
        print()
        if i == 2 or i == 5:
            print('---------------------')


def checkSafe(sudoku, row, col, num):
    # check row
    for j in range(9):
        if sudoku[row][j] == num:
            return False

    # check column
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # check current box
    row = row//3 *3
    col = col//3 *3
    for i in range(3):
        for j in range(3):
            if sudoku[i + row][j + col] == num:
                return False

    return True




def solve(sudoku, i = 0, j = 0):
    if i == 8 and j == 9:
        return True

    if j == 9:
        i += 1; j = 0

    if sudoku[i][j] > 0:
        return solve(sudoku, i, j+1)

    for x in range(1, 10):
        if checkSafe(sudoku, i, j, x):
            sudoku[i][j] = x
            if solve(sudoku, i, j+1):
                return True

    sudoku[i][j] = 0





if solve(sudoku):
    display(sudoku)
else:
    print("Not solvable")