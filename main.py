import sys, pygame
import gen_board
import time
from constants import *

pygame.init() #initializing pygame modules


def main():
    global screen

    #creat the screen and fill it with black color
    screen = pygame.display.set_mode(size)
    screen.fill(black)

    #Sudoku board needs to be in n^2*n^2 type format
    #you can call isValidBoard to check whether the
    #board is valid or not.
    board = gen_board.generateSudoku(int(num_blocks**0.5))

    for i in range(num_blocks):
       print(board[i])

    drawboard(board) #draw the board
    solve_sudoku(board)
    #game loop
    while True:
        for event in pygame.event.get(): #checking for exit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #updating the screen in each iteration
        pygame.display.update()

def drawboard(board):
    font = pygame.font.SysFont("Arial",25)
    row = col = 0
    drawing = []
    for x in range(0,width,blocksize):
        l = []
        for y in range(0,height,blocksize):

            # if board[i][j] is 0 then it is a blank space, represented by "?"
            # else it is a given number

            if board[x//blocksize][y//blocksize] != 0:
                # render returns a surface
                textSurface = font.render(str(board[x//blocksize][y//blocksize]),
                                          True, green)
                textRect = textSurface.get_rect()

                # repositioning it to it's correct place.
                textRect.update(x, y,
                                blocksize, blocksize)

                # drawing the text surface on the main screen.
                screen.blit(textSurface, textRect)
            else:
                textSurface = font.render("?", True, red)
                textRect = textSurface.get_rect()
                textRect.update(x, y,
                                blocksize, blocksize)
                screen.blit(textSurface, textRect)
        drawing.append(l)

import sys
sys.setrecursionlimit(10**6)


def find_empty_location(arr, l):
    for row in range(len(arr)):
        for col in range(len(arr)):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(len(arr)):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num):
    for i in range(len(arr)):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num):
    base = int((len(arr)**0.5))
    for i in range(base):
        for j in range(base):
            if(arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num):
    base = int((len(arr)**0.5))
    return (
        not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and
        not used_in_box(arr, row - row % base, col - col % base, num)
        )

def print_board(board):
    print("~~~~~~~~~~~~~~~~~")
    for i in board:
        print(*i)

def solve_sudoku(board):
    print_board(board)
    l =[0, 0]
    if(not find_empty_location(board, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, len(board) + 1):
        if(check_location_is_safe(board,
                          row, col, num)):
            board[row][col]= num
            redrawboard(board)
            time.sleep(0.2)
            if(solve_sudoku(board)):
                return True

            board[row][col] = 0
            redrawboard(board)
            time.sleep(0.2)
    return False




def redrawboard(board):
    screen.fill(black)
    font = pygame.font.SysFont("Arial",25)
    row = col = 0
    for x in range(0,width,blocksize):
        for y in range(0,height,blocksize):

            # if board[i][j] is 0 then it is a blank space, represented by "?"
            # else it is a given number

            if board[x//blocksize][y//blocksize] != 0:
                # render returns a surface
                textSurface = font.render(str(board[x//blocksize][y//blocksize]),
                                          True, green)
                textRect = textSurface.get_rect()

                # repositioning it to it's correct place.
                textRect.update(x, y,
                                blocksize, blocksize)

                # drawing the text surface on the main screen.
                screen.blit(textSurface, textRect)
            else:
                textSurface = font.render("?", True, red)
                textRect = textSurface.get_rect()
                textRect.update(x, y,
                                blocksize, blocksize)
                screen.blit(textSurface, textRect)
    pygame.display.update()


main()
