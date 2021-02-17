import sys, pygame
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

    #game loop
    while True:
        drawgrid() #draw a grid
        for event in pygame.event.get(): #checking for exit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #updating the screen in each iteration
        pygame.display.update()

def drawgrid():
    for x in range(width):
        for y in range( height):

            # creating a pygame Rect object
            # Rect(left , top, width, height)
            rect = pygame.Rect (x*blocksize, y*blocksize,
                                blocksize, blocksize)

            #drawing the rectangle
            pygame.draw.rect(screen, green, rect, 1)




main()
