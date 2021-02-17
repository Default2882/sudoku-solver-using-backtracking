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

            # creating a pygame Rect object
            # Rect(left , top, width, height)
            #rect = pygame.Rect (x*blocksize, y*blocksize,
            #                    blocksize, blocksize)
            if board[x//blocksize][y//blocksize] != 0:
                textSurface = font.render(str(board[x//blocksize][y//blocksize]),
                                          True, (0,255,0))
                textRect = textSurface.get_rect()
                textRect.update(x, y,
                                blocksize, blocksize)
                screen.blit(textSurface, textRect)
            else:
                textSurface = font.render("?",True, (255,0,0))
                textRect = textSurface.get_rect()
                textRect.update(x, y,
                                blocksize, blocksize)
                screen.blit(textSurface, textRect)
            #l.append(textRect)
            #print(x,y,row,col, x%blocksize,blocksize)
            #drawing the rectangle
            #pygame.draw.rect(screen, green, rect, 1)
            #if (y+1) % blocksize == 0:
            #    col += 1
            #    if col > num_blocks:
            #        row += 1
            #        col = 0
        drawing.append(l)
    #screen.fill(pygame.Color("black"))
    #for i in range(num_blocks):
    #    for j in rnage(num_blocks):


main()
