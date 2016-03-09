import pygame  # This imports all the pygame methods
import time   # This imports time functions

pygame.init()  # This initialize the methods

# Defining display variable
displayWidth = 600
displayHeight = 480
# Defining block and frame variables
blockSize = 10
fps = 15

# Rendering a font
font = pygame.font.SysFont(None, 25)

#Function for message display before quit
def messagetoScreen(msg, color):
    screentext = font.render(msg, True, color)
    gameDisplay.blit(screentext, [displayWidth/2, displayHeight/2])
# Display setmode sets the screen size
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# Display set caption give the name to the window
pygame.display.set_caption('Snake Me')

# Defining colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Defining frame
clock = pygame.time.Clock()


def gameLoop():
    # Defining the snake head
    lead_x = displayWidth / 2
    lead_y = displayHeight / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    while not gameExit:  # This is the main loop

        # This is section will ask if player wants to quit or play again
        while gameOver == True:
            gameDisplay.fill(white)
            messagetoScreen("Game over!! Press S to Start Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
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
                    lead_x_change = -blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = blockSize
                    lead_x_change = 0

        if lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change  # Using while loop for continuous movement
        lead_y += lead_y_change  # Using while loop for continuous movement
        gameDisplay.fill(white)  # This puts the background color
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, blockSize, blockSize])
        pygame.display.update()

        clock.tick(fps)  # This sets the frames per second

    messagetoScreen("You Lose", red)
    pygame.display.update()

    time.sleep(2)
    pygame.quit()
    quit()


gameLoop()