import random
from collections import defaultdict

# randomize rows, columns and numbers (of valid base pattern)
from random import sample

# pattern for a baseline valid solution
def pattern(r,c,base,side): return (base*(r%base)+r//base+c)%side

def shuffle(s,base): return sample(s,len(s))

def generateSudoku(base):
    rBase = range(base)
    side = base*base
    rows  = [ g*base + r for g in shuffle(rBase,base) for r in shuffle(rBase,base) ]
    cols  = [ g*base + c for g in shuffle(rBase,base) for c in shuffle(rBase,base) ]
    nums  = shuffle(range(1,base*base+1), base)

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c,base,side)] for c in cols] for r in rows ]
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    numSize = len(str(side))
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
            elif board[i][j] != "?":
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                box[boxindex].append(board[i][j])
    return True

