import sys, pygame
import gen_board
pygame.init() #initializing pygame modules

num_blocks = 9 #number of blocks in the grid
blocksize = 50 #blocksize
width = height = num_blocks*blocksize  #width and height
size = (width, height) #size of the screen
speed = [2, 2] #speed at which animation runs
black = (0, 0, 0) #RGB of black
green = (0, 255, 0) #RGB of green
red = (255, 0, 0)

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

    #game loop
    while True:
        drawgrid(board) #draw a grid
        for event in pygame.event.get(): #checking for exit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #updating the screen in each iteration
        pygame.display.update()

def drawgrid(board):
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


main()
