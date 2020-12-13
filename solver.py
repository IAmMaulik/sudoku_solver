def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if isValid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            
            # Backtracking
            bo[row][col] = 0
    return False


# Printing the board out
def print_board(bo):
    for i in range (len(bo)):
        if (i%3)==0 and i!=0:
            print("= = = = = = = = = = = = ")

        for j in range(len(bo[0])):
            if (j%3)==0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


# Finding empty squares on the sudoku board
def find_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo[0])):
            if bo[x][y] == 0:
                return (x, y) # Coordinates of the empty square
    return None


# Is the position valid or not
def isValid(bo, num, pos):
    # Checking the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1]!=i:
            return False
    
    # Checking the column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0]!=i:
            return False
    
    # Checking whether it is in the same box (Slightly tricky)
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j]==num and (i, j) != pos:
                return False    
    return True


# Defining the 2d array
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print_board(board)
solve(board)
print("\n\nSolution is:\n\n\n\n")
print_board(board)