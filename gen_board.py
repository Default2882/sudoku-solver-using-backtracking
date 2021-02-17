import random
from collections import defaultdict


def generateSudoku(num_blocks):
    # "." represents empty block
    board = [["."]*num_blocks]*num_blocks
    while True:
        for i in range(num_blocks):
            for j in range(num_blocks):
                curr_val = random.randrange(1,num_blocks+1)
                board[i][j] = curr_val
        if isValidBoard(board):
            break
        else:
            print("Not valid!")

    return board



def isValidBoard(board):
    box = defaultdict(list)
    row = defaultdict(list)
    col = defaultdict(list)
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            boxindex = (i//3)*3 + j//3
            if (
                board[i][j] in row[i] or
                board[i][j] in col[j] or
                board[i][j] in box[boxindex]
                ):
                return False
            elif board[i][j] != ".":
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                box[boxindex].append(board[i][j])
    return True

print(generateSudoku(9))
