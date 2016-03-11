import pygame  # This imports all the pygame methods
import time   # This imports time functions
import random   # This is random apple apearance on the screen

pygame.init()  # This initialize the methods

# Defining display variable
displayWidth = 600
displayHeight = 480

# Defining block and frame variables
blockSize = 29
fps = 15

direction = "right"

# Rendering a font
font = pygame.font.SysFont(None, 25)

#this is to center the text after game is over
def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Function for message display before quit
def messagetoScreen(msg, color):
    #screentext = font.render(msg, True, color)
    #gameDisplay.blit(screentext, [displayWidth/2, displayHeight/2])
    textSurface, textRect = text_objects(msg, color)
    textRect.center = (displayWidth / 2), (displayHeight / 2)
    gameDisplay.blit(textSurface, textRect)


#Function to draw the snake
def snake(blockSize, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    elif direction == "left":
        head = pygame.transform.rotate(img, 90)
    elif direction == "up":
        head = img
    elif direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], blockSize, blockSize])

# Display setmode sets the screen size
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# Display set caption give the name to the window
pygame.display.set_caption('Snake Me')


img = pygame.image.load('snakehead2.png')


# Defining colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (42, 132, 7)

# Defining frame
clock = pygame.time.Clock()


def gameLoop():

    #Global direction

    global direction
    # Defining the snake head
    lead_x = displayWidth / 2
    lead_y = displayHeight / 2
    lead_x_change = 0
    lead_y_change = 0

    #snakeList should not refresh under while loop
    snakeList = []
    snakeLength = 1

    # Rounding it to the value to 10 so that it appear correct in aligned to the snake
    randAppleX = round(random.randrange(0, displayWidth-blockSize))#/10.0)*10.0
    randAppleY = round(random.randrange(0, displayHeight-blockSize))#/10.0)*10.0

    gameExit = False
    gameOver = False

    while not gameExit:  # This is the main loop

        # This is section will ask if player wants to quit or play again
        while gameOver == True:
            gameDisplay.fill(white)
            messagetoScreen("Game over!! Press S to Start Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_s:
                        gameLoop()


        for event in pygame.event.get():  # This fetches all the events like keyup, mousemove
            if event.type == pygame.QUIT:  # For all other types of events refer to pygameEvent.txt
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -blockSize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = blockSize
                    lead_x_change = 0

        if lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change  # Using while loop for continuous movement
        lead_y += lead_y_change  # Using while loop for continuous movement
        gameDisplay.fill(white)  # This puts the background color

        appleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # This is to control the snakelenght
        if len(snakeList) > snakeLength:
            del snakeList[0]


        # This is for crashing the snake to itself
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(blockSize, snakeList)
        pygame.display.update()

        #if lead_x == randAppleX and lead_y == randAppleY:
        #if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
        #    if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
        #        randAppleX = round(random.randrange(0, displayWidth-blockSize))#/10.0)*10.0
        #        randAppleY = round(random.randrange(0, displayHeight-blockSize))#/10.0)*10.0
        #        snakeLength += 1


        # cross over code this would ensure cross over works
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + blockSize> randAppleX and lead_x + blockSize < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + blockSize> randAppleY and lead_y + blockSize < randAppleY + appleThickness:
                randAppleX = round(random.randrange(0, displayWidth-blockSize))#/10.0)*10.0
                randAppleY = round(random.randrange(0, displayHeight-blockSize))#/10.0)*10.0
                snakeLength += 1

        clock.tick(fps)  # This sets the frames per second

    messagetoScreen("You Lose", red)
    pygame.display.update()

    time.sleep(2)
    pygame.quit()
    quit()


gameLoop()