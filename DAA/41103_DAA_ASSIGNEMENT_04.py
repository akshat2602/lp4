global n

def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    i, j = row + 1, col + 1
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solvenQUtil(board, col):
    if col >= n:
        return True
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solvenQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False


def solvenQ():
    board = []
    global n
    n = int(input("Enter the number of queens : "))
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(0)
        board.append(temp)
    if solvenQUtil(board, 0) == False:
        print("Solution does not exist") 
        return False

    printSolution(board)
    return True


solvenQ()
